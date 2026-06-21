from django.urls import path

from authentication.v1.views.auth import ManagerRegisterView, ManagerLoginView

urlpatterns = [
    path("register", ManagerRegisterView.as_view()),
    path("login", ManagerLoginView.as_view()),
]