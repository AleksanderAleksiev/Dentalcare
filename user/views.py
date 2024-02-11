from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from utils.utils import check_for_insufficient_props
from rest_framework.decorators import api_view


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data

            props_to_check_for = ['name', 'email', 'password', 'phone', 'address', 'years', 'image', 'is_dentist']

            if check_for_insufficient_props(data, props_to_check_for):
                return Response(
                    {'error': 'You have not specified enough fields for the user'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            phone = data['phone']
            years = data['years']
            address = data['address']
            image = data['image']

            is_dentist = str(data['is_dentist'])


            if is_dentist == 'True':
                is_dentist = True
            else:
                is_dentist = False

            if not User.objects.filter(email=email).exists():
                if not is_dentist:
                    User.objects.create_user(name=name, email=email, password=password, phone=phone, years=years, address=address, image=image)

                    return Response(
                        {'success': 'User created successfully'},
                        status=status.HTTP_201_CREATED
                    )
                else:
                    User.objects.create_dentist(name=name, email=email, password=password, phone=phone, years=years, address=address, image=image)

                    return Response(
                        {'success': 'Dentist account created successfully'},
                        status=status.HTTP_201_CREATED
                    )
            else:
                return Response(
                    {'error': 'User with this email already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

        
    def put(self, request, format=None):
        try:
            data = request.data

            props_to_check_for = ['name', 'email', 'phone', 'address', 'years', 'image']

            if check_for_insufficient_props(data, props_to_check_for):
                return Response(
                    {'error': 'You have not specified enough fields for the user'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if request.user.email != data['email']:
                return Response(
                    {'error': 'You do not have necessary permissions to edit this user'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            name = data['name']
            email = data['email']
            phone = data['phone']
            address = data['address']
            years = data['years']
            image = data['image']
            image = 'user/assets/images/' + str(image)


            User.objects.filter(email=email).update(
                name=name,
                phone=phone,
                address=address,
                years=years,
                image=image,
            )

            return Response(
                {'success': 'User account updated successfully'},
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            print(e)

            return Response(
                {'error': 'Something went wrong when updating user account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


@api_view(['GET'])
def get_all_dentists(request):

    try:
        data = User.objects.filter(is_dentist=True)

        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(
            {'dentists': serializer.data},
            status=status.HTTP_200_OK
        )
    
    except Exception as e:
        print(e)

        return Response(
            {'error': 'Something went wrong when retrieving dentist users'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    


@api_view(['GET'])
def get_user_detail(request, id):

    try:
        user = User.objects.get(id=id)

        serializer = UserSerializer(user, context={'request': request})

        return Response(
            {'user': serializer.data},
            status=status.HTTP_200_OK,
        )

    except User.DoesNotExist:
        return Response(
            {'error': 'User does not exist'},
            status=status.HTTP_404_NOT_FOUND,
        )
    
    except Exception as e:
        print(e)

        return Response(
            {'error': 'Something went wrong when retrieving user details'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ) 