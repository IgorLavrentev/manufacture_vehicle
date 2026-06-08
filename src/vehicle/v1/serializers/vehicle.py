from rest_framework import serializers

from vehicle.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ['name', 'cost', 'year',"mileage"]

        # extra_kwqrgs = {
        #     "enterprise": {
        #         "is_null": True
        #     }
        # }
