from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
   title = models.CharField(max_length=255)
   summary = RichTextUploadingField()
   content = RichTextUploadingField()
   author = models.ForeignKey(User, on_delete=models.PROTECT)
   created_at = models.DateField(auto_now_add=True)
