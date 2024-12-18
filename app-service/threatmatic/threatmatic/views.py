from django.http import Http404, JsonResponse, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics
from datetime import datetime
from django.db.models import OuterRef, Subquery, Max
from .models import (Devicelist, Fortinetlogs)
from .serializer import (DevicelistSerializer, 
                         FortinetlogsSerializer)
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User

class DeviceListAPIView(generics.ListAPIView):
  serializer_class = DevicelistSerializer
  def get_queryset(self):
    try:
      all_devices = Devicelist.objects.all()
      return all_devices
    except Exception as e:
      print(e)
      return Response({'error': 'Something went wrong'}, status=500)
class FortinetlogsListAPIView(generics.ListAPIView):
  serializer_class = FortinetlogsSerializer
  filter_backends = [DjangoFilterBackend]
  def get_queryset(self):
    try:
      all_logs = Fortinetlogs.objects.all()
      dev_ip = self.request.GET.get('devip')
      start_time = self.request.GET.get('start_time')
      end_time = self.request.GET.get('end_time')
      filtered_logs = None
      if start_time and end_time:
        # Convert to datetime objects
        start_time = datetime.fromisoformat(start_time) if start_time else None
        end_time = datetime.fromisoformat(end_time) if end_time else None
        filtered_logs = all_logs.filter(timestamp__range=(start_time, end_time),
                                                devip=dev_ip).order_by('-timestamp')
      else:
        filtered_logs = all_logs.filter(devip=dev_ip).order_by('-timestamp')
      return filtered_logs
    except Exception as e:
      print(e)
      return Response({'error': 'Something went wrong'}, status=500)