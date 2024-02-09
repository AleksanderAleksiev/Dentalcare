from rest_framework.decorators import api_view
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.utils import check_for_insufficient_props


@api_view(['GET'])
def get_feedback_all(request):

    try:
        data = Feedback.objects.all()

        serializer = FeedbackSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    except:
        return Response(
            {'error': 'Could not get all types of feedback'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET'])
def get_user_feedback(request):

    try:
        user = request.user

        feedback = Feedback.objects.filter(created_by=user.id)

        serializer = FeedbackSerializer(feedback, many=True)

        return Response(
            {'feedback': serializer.data},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print(e)        
        return Response(
            {'error': 'Something went wrong when retrieving user feedback'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(['GET'])
def get_dentist_feedback(request, id):

    try:
        feedback = Feedback.objects.filter(dentist=id)

        serializer = FeedbackSerializer(feedback, many=True)

        return Response(
            {'feedback': serializer.data},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        print(e)        
        return Response(
            {'error': 'Something went wrong when retrieving dentist feedback'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    


@api_view(['POST'])
def create_feedback(request):
    try:
        data = request.data

        props_to_check_for = ['text', 'created_by', 'dentist']

        if check_for_insufficient_props(data, props_to_check_for):
            return Response(
                {'error': 'You have not specified enough fields for the feedback'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = FeedbackSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {'success': 'Feedback created successfully'},
                status=status.HTTP_201_CREATED,
            )

    except:
        return Response(
            {'error': 'Something went wrong when creating feedback'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    


@api_view(['PUT', 'DELETE'])
def feedback_detail(request, id):
    try:
        feedback = Feedback.objects.get(id=id)

        action = 'update' if request.method == 'PUT' else 'delete' 

        if feedback.created_by != request.user:
            return Response(
                {'error': f'You do not have permissions to {action} this feedback'}
            )

        if request.method == 'PUT':

            data = request.data

            props_to_check_for = ['text', 'created_by', 'dentist']

            if check_for_insufficient_props(data, props_to_check_for):
                return Response(
                    {'error': 'You have not specified enough fields for the feedback'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer = FeedbackSerializer(feedback, data=data, context={'request': request})

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {'success': 'Feedback updated successfully'},
                    status=status.HTTP_200_OK,
                )
            
        elif request.method == 'DELETE':

            feedback.delete()

            return Response(
                {'success': 'Feedback deleted successfully'},
                status=status.HTTP_204_NO_CONTENT,
            )

    except Feedback.DoesNotExist:
        return Response(
            {'error': 'Feedback does not exist'},
            status=status.HTTP_404_NOT_FOUND,
        )
      
    except Exception as e:
        print(e)
        
        return Response(
            {'error': f'Something went wrong when trying to {action} feedback'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )