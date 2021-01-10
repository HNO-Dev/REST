from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import HelloSerializer,UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile 
from rest_framework.authentication import TokenAuthentication
# Create your views here.
class HelloApiView(APIView):


    serializer_class=HelloSerializer
    
    def get(self,request,format=None):
        wert=['olami','sam','hillary']

        return Response({'message':'holla','content':wert})

    def post(self,request):
        serializer=HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,pk=None):
        """updating an object"""
        
        return Response({'method':'put'})


    def patch(self,request,pk=None):
        """"only updates fields provided in the request"""

        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        """"delete an object """

        return Response({'method':'delete'})




class HelloViewset(viewsets.ViewSet):

    serializer_class=HelloSerializer


    def list(self,request):
        a_vieew=['ásd','asas']

        return Response({'message':'hello','a_vieew':a_vieew})

    def create(self,request):

        serializer=HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello{0}'.format(name)
            return Response({'message':message})


        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrieve(self,request,pk=None):
        
        return Response({'method':'get'})


    def update(self,request,pk=None):

        return Response({'method':'put'})

    
    def partial_update(self,request,pk=None):

        return Response({'method':'patch'})

    def destroy(self,request,pk=None):
        """"delete an object """
        return Response({'method':'delete'})
    





class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class=UserProfileSerializer
    queryset=UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)



