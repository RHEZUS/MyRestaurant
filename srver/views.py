from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.http import HttpResponse

from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from users.models import User
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def welcome_view(request):
    return HttpResponse("Welcome to api.ludivsolutions.tech")

#@api_view(['POST'])
#def login(request):
#    email=request.data['email']
#    user = get_object_or_404(User, email=email)
#    print("the user: {} was found".format(user))
#    if not user.check_password(request.data['password']):
#        print("Users with email: {} not found.".format(user))
#        return Response({"details": "Not found"}, status=status.HTTP_404_NOT_FOUND)
#    token, created = Token.objects.get_or_create(user=user)
#    serializer = UserSerializer(instance=user)
#    return Response({"token":token.key, "user": serializer.data})

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if email is None or password is None:
        return Response({"details": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    print(f"Authenticating user with email: {email}")
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data})
    else:
        # Check if the user exists with the provided email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"details": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the provided password is correct
        if not user.check_password(password):
            return Response({"details": "Invalid password."}, status=status.HTTP_401_UNAUTHORIZED)
        
        # If the user exists and the password is incorrect, return unauthorized
        return Response({"details": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user))
