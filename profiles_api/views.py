from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

<<<<<<< HEAD
<<<<<<< Updated upstream
from rest_framework import viewsets

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
=======
>>>>>>> Stashed changes
=======
<<<<<<< HEAD
from rest_framework import viewsets

=======
>>>>>>> d98eea2a42c8948a0709e607b6256b4139660220
>>>>>>> 17327c535d5e3d4120fe74814adc3699f14f9291

# Create your views here.

class HelloApiView(APIView):
    """Test API VIEW"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< Updated upstream
        
=======
<<<<<<< HEAD
<<<<<<< HEAD
        return Response({'method': 'DELETE'})
=======
        return Response({'method': 'DELETE'})
>>>>>>> parent of 2899471... VIEW SET
=======
>>>>>>> Stashed changes
        return Response({'method': 'DELETE'})
=======

>>>>>>> 17327c535d5e3d4120fe74814adc3699f14f9291

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

<<<<<<< HEAD
        return Response({'http_method': 'DELETE'})
<<<<<<< HEAD
<<<<<<< Updated upstream

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    ...
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
=======
=======
        return Response({'method': 'DELETE'})
>>>>>>> parent of 2899471... VIEW SET
=======
        return Response({'method': 'DELETE'})
>>>>>>> parent of 2899471... VIEW SET
>>>>>>> Stashed changes
=======
=======
        return Response({'http_method': 'DELETE'})
>>>>>>> d98eea2a42c8948a0709e607b6256b4139660220
>>>>>>> 17327c535d5e3d4120fe74814adc3699f14f9291
