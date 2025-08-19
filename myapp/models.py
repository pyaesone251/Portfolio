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

class ResumeEducation(models.Model):
    maintitle = RichTextField(null=True,blank=True)
    subtitle = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    experience = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class EducationExperience(models.Model):
    title = RichTextField(null=True,blank=True)
    year = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class PortfolioAera(models.Model):
    title = RichTextField(null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class Portfolio(models.Model):
    image = models.ImageField(upload_to='image',null=True,blank=True)
    title = RichTextField(null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class BlogAera(models.Model):
    title = RichTextField(null=True,blank=True)
    name = RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)

class Blog(models.Model):
    image1 = models.ImageField(upload_to='blog',null=True,blank=True)
    image2 = models.ImageField(upload_to='blog',null=True,blank=True)
    date = RichTextField(null=True,blank=True)
    people = RichTextField(null=True,blank=True)
    comment = RichTextField(null=True,blank=True)
    title = RichTextField(null=True,blank=True)
    note = RichTextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updeated_at = models.DateTimeField(auto_now=True)
    


