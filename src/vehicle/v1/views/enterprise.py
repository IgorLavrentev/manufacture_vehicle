from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from vehicle.models import Enterprise
from vehicle.v1.serializers.enterprise import EnterpriseSerializer
from rest_framework.exceptions import APIException


class UserEnterpriseForbiddenError(APIException):
    status_code = 403
    default_detail = "forbidden for this user"


class EnterpriseList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




class EnterpriseDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsAuthenticated]

    def get_user_enterprises(self, user):
        return user.enterprises.all().values_list("id", flat=True)


    def get(self, request, *args, **kwargs):
        user_enterprises = self.get_user_enterprises(request.user)

        if kwargs["pk"] not in user_enterprises:
            raise UserEnterpriseForbiddenError
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)