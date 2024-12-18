from rest_framework import serializers
from .models import (Devicelist, Fortinetlogs)


class DevicelistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Devicelist
    fields = "__all__"

class FortinetlogsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fortinetlogs
    fields = "__all__"