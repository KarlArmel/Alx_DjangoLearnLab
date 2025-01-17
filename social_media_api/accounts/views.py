from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from .models import CustomUser  # Assuming CustomUser is your user model
from .serializers import RegisterSerializer, UserSerializer

# Use CustomUser if it's your user model
User = CustomUser  # Or use get_user_model() if you're dynamically using the default user model

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    if user_to_follow == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)  # Ensure the `following` field is part of the CustomUser model
    return Response({"detail": f"Now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    if user_to_unfollow == request.user:
        return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)  # Same as above, ensure `following` is a valid field
    return Response({"detail": f"Unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# If you're using a generics view, here's an example
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # Ensure CustomUser is being referenced here
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # This ensures only authenticated users can access this endpoint

class Generics(generics.GenericAPIView):
    queryset = CustomUser.objects.all()  # Ensure CustomUser is being referenced here
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # This ensures only authenticated users can access this endpoint
