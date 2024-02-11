from rest_framework.decorators import api_view
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from utils.utils import check_for_insufficient_props


@api_view(['GET'])
def get_all_appointments(request):

    try:
        data = Appointment.objects.all()

        serializer = AppointmentSerializer(data, context={'request': request}, many=True)

        return Response(
            {'appointments': serializer.data},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print(e)

        return Response(
            {'error': 'Something went wrong when retrieving appointments'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



def get_appointments_by_date_range(start_date, end_date, dentist_id, patient_id):

    dentist_appointments = []
    
    if dentist_id:
        dentist_appointments = Appointment.objects.filter(dentist=dentist_id)
    
    patient_appointments = []

    if patient_id:
        patient_appointments = Appointment.objects.filter(patient=patient_id)

    filtered_appointments = []

    appointments = list(dentist_appointments) + list(patient_appointments)

    appointments = list(set(appointments))

    for appointment in appointments:
        appointment.start_date = appointment.start_date.replace(tzinfo=None)
        appointment.end_date = appointment.end_date.replace(tzinfo=None)

        if (appointment.start_date >= start_date and appointment.start_date < end_date) or (appointment.end_date > start_date and appointment.end_date <= end_date) or (appointment.start_date <= start_date and appointment.end_date >= end_date):
            filtered_appointments.append(appointment)

    return filtered_appointments


@api_view(['GET'])
def get_user_appointments_by_date_range(request):

    try:
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']
        
        dentist_id = ''

        if request.query_params and 'dentist' in request.query_params:
            dentist_id = request.query_params['dentist']

        if start_date == '' or start_date == None:
            return Response(
                {'error': 'No Start Date Provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if end_date == '' or end_date == None :
            return Response(
                {'error': 'No End Date Provided'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        if start_date >= end_date:
            return Response(
                {'error': 'Start date is later than End date'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user

        if user.is_dentist:
            user_params = {
                'dentist_id': user.id,
                'patient_id': ''
            }
        else:
            user_params = {
                'dentist_id' : dentist_id,
                'patient_id': user.id
            }

        filtered_appointments = get_appointments_by_date_range(start_date, end_date, user_params['dentist_id'], user_params['patient_id'])

        serializer = AppointmentSerializer(filtered_appointments, many=True)

        return Response(
            {'appointments': serializer.data},
            status=status.HTTP_200_OK
        )
    
    except ValueError:
        return Response(
            {'error': 'Start date or End date are not in correct format'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        print(e)

        return Response(
            {'error': 'Something went wrong when retrieving user appointments'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



@api_view(['POST'])
def create_appointment(request):
    try:
        data = request.data

        props_to_check_for = ['title', 'description', 'start_date', 'end_date', 'patient', 'dentist', 'is_all_day', 'recurrence_rule', 'excluded_dates']

        if check_for_insufficient_props(data, props_to_check_for):
            return Response(
                {'error': 'You have not specified enough fields for the appointment'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        start_date = data['start_date']
        end_date = data['end_date']

        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        if start_date >= end_date:
            return Response(
                {'error': 'Start date is later than End date'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if start_date < datetime.now():
            return Response(
                {'error': 'Start date has already passed'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        dentist_id = data['dentist']
        patient_id = data['patient']       

        filtered_appointments = get_appointments_by_date_range(start_date, end_date, dentist_id, patient_id)

        if filtered_appointments != []:
            return Response(
                {'error': 'There is a conflicting appointment. Adjust your selected time'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        serializer = AppointmentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {'success': 'Appointment created successfully'},
                status=status.HTTP_201_CREATED,
            )
        
    except ValueError:
        return Response(
            {'error': 'Start date or End date are not in correct format'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        print(e)

        return Response(
            {'error': 'Something went wrong when creating an appointment'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



@api_view(['PUT', 'DELETE'])
def appointment_detail(request, id):
    try:
        appointment = Appointment.objects.get(id=id)

        if request.method == 'PUT':

            data = request.data

            props_to_check_for = ['title', 'description', 'start_date', 'end_date', 'patient', 'dentist', 'is_all_day', 'recurrence_rule', 'excluded_dates']

            if check_for_insufficient_props(data, props_to_check_for):
                return Response(
                    {'error': 'You have not specified enough fields for the appointment'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            start_date = data['start_date']
            end_date = data['end_date']

            start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%fZ')
            end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S.%fZ')

            if start_date >= end_date:
                return Response(
                    {'error': 'Start date is later than End date'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            if start_date < datetime.now():
                return Response(
                    {'error': 'Start date has already passed'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            dentist_id = data['dentist']
            patient_id = data['patient']            

            filtered_appointments = get_appointments_by_date_range(start_date, end_date, dentist_id, patient_id)
            filtered_appointments = list(filter(lambda appointment: appointment.id != id, filtered_appointments))

            if filtered_appointments != []:
                return Response(
                    {'error': 'There is a conflicting appointment. Adjust your selected time'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            

            serializer = AppointmentSerializer(appointment, data=data, context={'request': request})

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {'success': 'Appointment updated successfully'},
                    status=status.HTTP_200_OK,
                )
            
        elif request.method == 'DELETE':

            user = request.user

            if (user.is_dentist and user.id != appointment.dentist.id) or ((not user.is_dentist) and user.id != appointment.patient.id): 
                return Response(
                    {'error': 'You do not have permissions to delete this appointment'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            appointment.delete()

            return Response(
                {'success': 'Appointment deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )


    except Appointment.DoesNotExist:
        return Response(
            {'error': 'Appointment does not exist'},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    except ValueError:
        return Response(
            {'error': 'Start date or End date are not in correct format'},
            status=status.HTTP_400_BAD_REQUEST,
        )
      
    except Exception as e:
        print(e)

        action = 'update' if request.method == 'PUT' else 'delete' 
        
        return Response(
            {'error': f'Something went wrong when trying to {action} appointment'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
