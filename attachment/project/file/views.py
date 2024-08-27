from django.shortcuts import render
from rest_framework.response import Response
from multiattachment1.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.contenttypes.models import ContentType
import pandas as pd
from django.conf import settings
import uuid
import os

class ExportImportExcelViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset=LeaveApply.objects.all()
        serializer=FileUploadSerializer(queryset,many=True)
        df=pd.DataFrame(serializer.data)
        print(df)
        save_directory = "C:/Users/Mishaa/Downloads/PLRA_Practice/"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        file_path=os.path.join(save_directory, f"{uuid.uuid4()}.csv")
        df.to_csv(file_path, encoding="UTF-8", index=False)
        print(f"File saved to {file_path}")

        return Response({'status':200})

    def create(self,request):
        file_upload_obj=FileUpload.objects.create(file_upload_csv=request.FILES['files'])
        df=pd.read_csv(f"{settings.BASE_DIR}C:/Users/Mishaa/Downloads/PLRA_Practice/{file_upload_obj.file_upload_csv}")
        for leave in LeaveApply:
            print(leave)

        return Response({'status':200})

# class ExportImportExcelViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['get'])
#     def export(self, request):
#         model_name = request.data.get('model_name')
#         if not model_name:
#             return Response({'error': 'Model name is required'}, status=400)

#         try:
#             model = ContentType.objects.get(model=model_name).model_class()
#         except ContentType.DoesNotExist:
#             return Response({'error': 'Invalid model name'}, status=400)
#         queryset=model.objects.all()
#         serializer=FileUploadSerializer(data=request.data,many=True)
#         df=pd.DataFrame(serializer.data)
#         print(df)

        # return Response({'status':200})


