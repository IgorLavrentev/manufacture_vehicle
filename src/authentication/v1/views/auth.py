from audioop import reverse


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from account.models import Manager
from authentication.v1.serializers.auth import ManagerAuthSerializer


class ManagerRegisterView(
    generics.GenericAPIView
):
    serializer_class = ManagerAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Manager.objects.create_user(
            email=serializer.data.get("email"),
            password=serializer.data.get("password"))
        return Response(status.HTTP_201_CREATED)

class ManagerLoginView(
    generics.GenericAPIView
):
    serializer_class = ManagerAuthSerializer
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)


        user = authenticate(
            request,
            username=serializer.data.get("email"),
            password=serializer.data.get("password")
        )

        if user:
            login(request, user)
            return Response(status.HTTP_200_OK)
        else:
            raise AuthenticationFailed