from django.db import models
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F
from datetime import datetime


class Business(models.Model):
    business_name = models.CharField(max_length=200, null=True)
    credit = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.business_name


class Customer(models.Model):
    name = models.CharField(null=True, max_length=200)
    business_name = models.ForeignKey(Business, default=None, on_delete=models.SET_DEFAULT, null=True)
    charge = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    charge_time = models.DateTimeField()

    def __str__(self):
        return self.name





