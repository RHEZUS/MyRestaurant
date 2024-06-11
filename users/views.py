from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users.middleware import AdminRoleMiddleware
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_list(request):
    """
    Handle GET and POST requests for User list.

    GET: Retrieve a list of all users.
    POST: Create a new user.
    """
    admin_middleware = AdminRoleMiddleware(None)  # Initialize with None as get_response
    response = admin_middleware(request)
    if response:
        return response
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')  # Retrieve username from request data
            password = request.data.get('password')  # Retrieve password from request data
            email = request.data.get('email')
            role = request.data.get('role')
            if not username or not password:
                return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create a new user with the provided username and password
            user = User.objects.create_user(username=username, password=password, email=email, role=role)
            return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    """
        Handle GET, PUT, and DELETE requests for a specific User.

        GET: Retrieve details of a specific user.
        PUT: Update an existing user.
        DELETE: Delete an existing user.
    """
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def login(request):
    """
    Handle POST request for user login.

    POST: Authenticate user credentials and generate token for logged-in user.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    
    if email is None or password is None:
        return Response({"details": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    print(f"Authenticating user with email: {email}")
    user = get_object_or_404(User, email=email)
    #user = authenticate(request, email=email, password=password)
    print(f"Authenticating user with email: {user}")
    if user is not None:
        print("user found: {}".format(user))
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
    """
    Handle POST request for user signup.

    POST: Create a new user and generate token for the user.
    """
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
    #print("Searching for token...")
    user = UserSerializer(request.user)
    return Response({"user":user.data})