from django.shortcuts import render
from .models import LeaveApply, LeaveAttachment
from .serializers import LeaveApplySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

class LeaveApplyViewSet(viewsets.ModelViewSet):
    queryset = LeaveApply.objects.all()
    serializer_class = LeaveApplySerializer

    def create(self,request):
         serializer=self.get_serializer(data=request.data)
         
         if serializer.is_valid(raise_exception=True):
              instance=serializer.save()
              print("instance",instance)
              attachment_data=request.FILES.getlist('attachment')
              print("attachment data to be uploaded",attachment_data)

              for attach in attachment_data:
                   uploaded=LeaveAttachment.objects.create(leaveapply=instance, attachment=attach)
                   print("uploaded",uploaded)
                #    result= LeaveApplySerializer(uploaded)
                #    serializer.save()

              return Response({'success': True, 'detail': 'Leave applied successfully.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        attachments_data = request.data.pop('attachment', [])
        instance = serializer.save()
        instance.attachment.all().delete()
        for data in attachments_data:
            LeaveAttachment.objects.create(leaveapply=instance, data=data)
        return Response(serializer.data)
