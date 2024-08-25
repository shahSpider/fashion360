from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from datetime import datetime, date
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    creation = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, blank=True)
    phone = models.CharField(
        max_length=15,
        validators= [
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete = models.CASCADE,
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    creation = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contact_assigned')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Lead(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    phone = models.CharField(
        max_length=15,
        validators= [
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    SOURCE_CHOICES = {
        "Facebook": "Facebook",
        "Instagram": "Instagram",
        "LinkedIn": "LinkedIn",
        "Website": "Website",
        "Friends": "Friends"
    }
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default="Website",
    )

    STATUS_CHOICES = {
        "New": "New",
        "Contacted": "Contacted",
        "Converted": "Converted",
        "Lost": "Lost",
    }
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="New"
    )
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_assigned')
    creation = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lead_created')

    def __str__(self) -> str:
        return self.name


class Opportunity(models.Model):
    name=models.CharField(max_length=60)
    customer=models.ForeignKey("Customer", on_delete=models.CASCADE)
    value=models.DecimalField(max_digits=10, decimal_places=2)
    currency=models.CharField(max_length=3, default='USD')
    
    STAGE_CHOICS = {
        "Prospecting": "Prospecting",
        "Qualification": "Qualification",
        "Proposal": "Proposal",
        "Negotiation": "Negotiation",
        "Closed Won": "Close d Won",
        "Closed Lost": "Closed Lost" 
    }
    stage=models.CharField(max_length=20, choices=STAGE_CHOICS, default="Prospecting")
    closing_date = models.DateField(default=timezone.now)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='opportunity_assigned')
    creation = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='opportunity_created')

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    activity_type = models.CharField(
        max_length=20,
        choices={
            "Call": "Call",
            "Meeting": "Meeting",
            "Email": "Email",
        },
        default="Call",
    )
    date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices={
            "Pending": "Pending",
            "Completed": "Completed",
            "Cancelled": "Cancelled",
        },
        default="Pending"
    )
    related_to = models.ForeignKey("Lead", on_delete=models.CASCADE, related_name='lead_related_to')

    def __str__(self) -> str:
        return self.title