# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='default.jpg')
    short_description=models.CharField(max_length=600,default='')
    complete_description=models.CharField(max_length=2000,default='')    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=300,default='')
    picture=models.ImageField(default='default.jpg')
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
    picture=models.ImageField(default='male.png')
    designation=models.CharField(max_length=400,default='')
    short_description=models.CharField(max_length=400,default='')
    complete_description=models.CharField(max_length=2000,default='')
    linkedinprofile=models.CharField(max_length=400,default='https://www.linkedin.com/company/al-nafi')
    def __str__(self):
        return self.name

class Contact(models.Model):
    First_Name=models.CharField(max_length=150)
    Last_Name=models.CharField(max_length=150)
    Business_Email=models.CharField(max_length=50)
    What_Are_You_Interested_In=models.CharField(max_length=50)
    How_Can_We_Help_You=models.CharField(max_length=400)
    def __str__(self):
        return self.First_Name

class Packages(models.Model):
    domain_name=models.CharField(max_length=300,default='')
    tool_name=models.CharField(max_length=300,default='')
    package_description=models.CharField(max_length=2000,default='')
    source=models.CharField(max_length=200,default='')    
    author=models.CharField(max_length=200,default='')    
    license=models.CharField(max_length=200,default='')    
    code=models.CharField(max_length=4000,default='')    
    usage_code=models.CharField(max_length=200,default='')    
    def __str__(self):
        return self.tool_name
