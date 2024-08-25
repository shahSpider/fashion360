from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(models.Model):
    role = models.CharField(max_length=50, choices=[
        ('sales', 'Sales'),
        ('customer_service', 'Customer Service'),
        ('system_manager', 'System Manager')
    ])

    def __str__(self):
        return self.role


class User(AbstractUser):
    role_profile = models.ForeignKey("UserProfile", on_delete=models.SET_NULL, null=True)


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    since_year = models.IntegerField()
    slogan = models.CharField(max_length=60)
    vision = models.TextField(max_length=400)

    def __str__(self):
        return self.company_name