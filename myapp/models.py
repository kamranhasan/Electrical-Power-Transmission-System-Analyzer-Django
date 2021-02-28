# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='anc.jpeg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name

class Audit_Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='anc.jpeg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name

class IS_Security_Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='anc.jpeg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name

class IS_Consultancy_Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='anc.jpeg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name


class Software_Solutions_Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='anc.jpeg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name




class Product(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='default_GE4BJy2.jpg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='male.png')
    designation=models.CharField(max_length=400,default='')
    description=models.CharField(max_length=400,default='')
    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(upload_to='https://storage.googleapis.com/nafi-consulting.appspot.com/media/',default='male.png')
    designation=models.CharField(max_length=400,default='')
    short_description=models.CharField(max_length=2000,default='')
    linkedinprofile=models.CharField(max_length=400,default='https://www.linkedin.com/company/al-nafi')
    def __str__(self):
        return self.name

class Contact(models.Model):
    First_Name=models.CharField(max_length=150)
    Last_Name=models.CharField(max_length=150)
    Contact_Number=models.CharField(max_length=20,blank=True, default='')
    Business_Email=models.CharField(max_length=50)
    How_Can_We_Help_You=models.CharField(max_length=400)
    def __str__(self):
        return self.First_Name

class Packages(models.Model):
    domain_name=models.CharField(max_length=100,default='')
    tool_name=models.CharField(max_length=300,default='')
    package_description=models.CharField(max_length=3000,default='')
    source=models.CharField(max_length=500,default='')    
    author=models.CharField(max_length=200,default='')    
    license=models.CharField(max_length=200,default='')    
    code=models.CharField(max_length=4000,default='')    
    usage_code=models.CharField(max_length=4000,default='')    
    def __str__(self):
        return self.tool_name
