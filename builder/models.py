from django.db import models

# Create your models here.

# model for handling file upload and saving in DB
class FileUpload(models.Model):
    file = models.FileField(upload_to="media", null=True, blank=True)
