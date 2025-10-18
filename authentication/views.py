import logging

from django.contrib.auth import authenticate, get_user_model
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import RegisterSerializer
from authentication.service import Cart

logger = logging.getLogger('authentication')

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'user': RegisterSerializer(user).data,
                    'message': 'User registered successfully'
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )

class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logger.info("Logout attempt received")
        try:
            refresh = request.data['refresh']
            token = RefreshToken(refresh)
            token.blacklist()
            logger.info(f"User logged out successfully: {refresh}")
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


class ProtectedAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        logger.info(f"Protected view accessed by: {request.user.username}")
        return Response({
            'message': 'This is a protected view',
            'user': request.user.username}, status=status.HTTP_200_OK)


class CartAPI(APIView):

    def get(self, request, format=None):
        cart = Cart(request)

        return Response(
            {"data": list(cart.__iter__()),
            "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

        elif "clear" in request.data:
            cart.clear()

        else:
            book = request.data
            cart.add(
                    book=book["book"],
                    quantity=book["quantity"],
                    overide_quantity=book["overide_quantity"] if "overide_quantity" in book else False
                )

        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED)
