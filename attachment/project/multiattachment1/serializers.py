from .models import *
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
def validate_file_size(file):
    max_size_kb = 3 * 1024 * 1024  # 3 MB
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"File size should not exceed {max_size_kb} KB")
    
class LeaveAttachmentSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(validators=[validate_file_size])
    class Meta:
        model = LeaveAttachment
        fields = '__all__'
    

class LeaveApplySerializer(serializers.ModelSerializer):
    attachment = LeaveAttachmentSerializer(many=True,read_only=True,required=False)
    # uploaded_attachments = serializers.ListField(
    #     child=serializers.FileField(allow_empty_file=False, use_url=False),
    #     required=False,
    #     write_only=True
    # )
    from_date = serializers.DateField()
    to_date = serializers.DateField()
    approved_date = serializers.DateField()
    report_back_date = serializers.DateField()
    apply_date=serializers.DateTimeField()
    class Meta:
        model = LeaveApply
        fields = '__all__'

    