from urllib.request import Request
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

from housing_operations.models import *
from housing_operations.serializers import *

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_new_house(request):
   serializer = HouseSerializer(data=request.data)
   account = Account.objects.get(user=request.user)
   data = {}
   if Account.is_landlord == True:
       if serializer.is_valid():
            serializer.save()
            data['response'] = f'Additional house added to {account.username} lot'
            return Response(data,status = status.HTTP_201_CREATED)
       else:
            data = serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
   if account.is_landlord == False:
        data['response'] = 'These measures are only allowed to landlords.'
        return Response(data,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_houses(request):
    data = {}
    houses = House.objects.all()
    data['houses'] = HouseSerializer(houses,many=True).data
    print(houses)

    return Response(data,status.HTTP_200_OK)

     

