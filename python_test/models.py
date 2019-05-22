from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from us import states


class Client(models.Model):
    """
    Client model
    """

    STATE_CHOICES = [(state.abbr, state.abbr) for state in states.STATES]

    name = models.CharField(max_length=256, null=False, blank=False, unique=True, help_text="Client name")
    contact_name = models.CharField(max_length=256, null=True, blank=True, help_text="Contact name")
    email = models.EmailField(null=False, blank=False, help_text="Email address")
    phone_number = PhoneNumberField(null=False, blank=False, help_text="Phone number")

    # address
    street_name = models.CharField(max_length=256, null=True, blank=True, help_text="Street name")
    suburb = models.CharField(max_length=256, null=True, blank=True, help_text="Street name")
    postcode = models.CharField(max_length=16, null=True, blank=True, help_text="Post code")
    state = models.CharField(max_length=2, null=True, blank=True, choices=STATE_CHOICES, help_text="State code")

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["suburb"]),
        ]
