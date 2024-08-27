from django.db import models


class FileUpload(models.Model):
    csv_file_upload = models.FileField(upload_to="csvfile")