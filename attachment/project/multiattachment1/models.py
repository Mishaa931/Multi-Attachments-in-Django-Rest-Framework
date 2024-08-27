from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=10)


class LeaveApply(models.Model):
    leave_request_id = models.AutoField(primary_key=True)
    leave_type=models.CharField(max_length=20, null=True)
    STATUS_CHOICES = [
        ("In Process", "In Process"),
        ("Approved", "Approved"),
        ("Withdraw", "Withdraw"),
        ("Rejected", "Rejected"),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hr_year_id = models.IntegerField(blank=True,null=True)
    apply_date = models.DateField(auto_now_add=True)  # Automatically set apply_date to the date and time of instance creation
    
    # Change related_name and remove null=True from leave_deduction_bucket_id
    leave_deduction_bucket_id = models.CharField(null=True, max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    days_count = models.IntegerField(blank=True)
    back_date = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="In Process")
    approved_date = models.DateField(blank=True, null=True)
    report_back_date = models.DateField(blank=True, null=True)
    notes = models.TextField()

class LeaveAttachment(models.Model):
    leaveapply = models.ForeignKey(LeaveApply, on_delete=models.CASCADE, related_name='apply_leave_attachments')
    def upload_path(instance, filename):
        return f'media/Leave/{filename}'
        # Construct the upload path with the employee's first name
    #     return f'media/{instance.employee.first_name+instance.employee.last_name}/Leave/{filename}'

    attachment = models.FileField(upload_to=upload_path, blank=True, null=True)
