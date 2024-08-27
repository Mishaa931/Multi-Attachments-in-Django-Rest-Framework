from rest_framework import serializers 
from .models import *

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        models=FileUpload
        fileds='__all__'