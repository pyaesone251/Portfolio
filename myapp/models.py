from django.db import models
from ckeditor. fields import RichTextField

# Create your models here.
class PositionModel(models.Model):
    image = models.ImageField(upload_to='image',null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    position = RichTextField(null=True,blank=True)
    phone = RichTextField(null=True,blank=True)
    email = RichTextField(null=True,blank=True)
    form = models.FileField(upload_to='cv_form',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class AboutModel(models.Model):
    maintitle = RichTextField(null=True,blank=True)
    subtitle = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class ServiceworkModel(models.Model):
    name = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    counter = RichTextField(null=True,blank=True)
    counter_para = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)



