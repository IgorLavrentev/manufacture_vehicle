from django.urls import path

from vehicle.v1.views.vehicle import VehicleList, VehicleDetail

urlpatterns = [
    path("", VehicleList.as_view()),
    path("<int:pk>/", VehicleDetail.as_view()),
]