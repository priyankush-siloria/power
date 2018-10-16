# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

	user = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE)
	number = models.CharField(max_length=100, blank=False, null=True)
	address = models.TextField(blank=True,null=True)
	city = models.CharField(max_length=200,blank=True,null=True)
	state = models.CharField(max_length=200,blank=True,null=True)
	country = models.CharField(max_length=200,blank=True,null=True)
	zipcode = models.CharField(max_length=200,blank=True,null=True)
	

class ContractorProfile(models.Model):

	user = models.OneToOneField(User, unique=True, blank=True, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, blank=False, null=True)
	number = models.CharField(max_length=50, blank=False, null=True)
	address = models.TextField(blank=True,null=True)
	companyname = models.TextField(blank=True,null=True)
	aboutcompany = models.TextField(blank=True,null=True)
	city = models.CharField(max_length=200,blank=True,null=True)
	state = models.CharField(max_length=200,blank=True,null=True)
	country = models.CharField(max_length=200,blank=True,null=True)
	zipcode = models.CharField(max_length=200,blank=True,null=True)
	
