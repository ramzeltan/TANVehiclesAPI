from dataclasses import field
from rest_framework import serializers
from . models import vehicls

class vehiclsSerializer(serializers.HyperlinkedModelSerializer):
  class meta:
    model = vehicls
    fields = ('name', 'description')