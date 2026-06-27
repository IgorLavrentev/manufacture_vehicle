from rest_framework import serializers

from vehicle.models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enterprise
        fields = ['name', 'city', 'address',"managers",'vehicle']