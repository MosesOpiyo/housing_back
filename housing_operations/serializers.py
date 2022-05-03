from rest_framework import serializers
from housing_operations.models import *

from housing_users.serializers import UserSerializer

class HouseSerializer(serializers.Serializer):
    landlord = UserSerializer(read_only=True)
    class Meta:
        model = House
        fields = '__all__'

    def save(self,request):
        house = House(name=self.validated_data['name'],
        address=self.validated_data['address'],
        house_category=self.validated_data['house_category'],
        number_of_bedrooms=self.validated_data['number_of_bedrooms'],
        apartments_spaces=self.validated_data['apartments_spaces'],
        apartments_available=self.validated_data['apartments_available'],
        house_image=self.validated_data['house_image'],
        livingroom_image=self.validated_data['livingroom_image'],
        kitchen_image=self.validated_data['kitchen_image'],
        sanitaryroom_image=self.validated_data['sanitaryroom_image'],
        bathroom_image=self.validated_data['bathroom_image'],
        bedroom_image=self.validated_data['bathroom_image'],
        landlord=request.user
        )
        house.save()
        return house 