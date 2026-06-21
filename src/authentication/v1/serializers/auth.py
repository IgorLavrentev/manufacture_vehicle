from rest_framework import serializers

from account.models import Manager


class ManagerAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ['email', 'password']
