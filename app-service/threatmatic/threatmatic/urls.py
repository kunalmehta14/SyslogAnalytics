from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import (FortinetlogsListAPIView, DeviceListAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/',
         DeviceListAPIView.as_view(), name='devices'),
    path('logs/',
    FortinetlogsListAPIView.as_view(), name='logs'),
]
