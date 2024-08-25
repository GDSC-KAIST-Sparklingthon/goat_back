from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/', UserView.as_view(), name='user'),
]
