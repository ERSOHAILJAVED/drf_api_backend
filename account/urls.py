from django.urls import path
from .views import UserResigisterView

urlpatterns = [
    path("registration/", UserResigisterView.as_view(), name="registration"),
]