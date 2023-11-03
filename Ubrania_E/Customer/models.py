from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    mobile = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    # Other fields...
    dob = models.DateField()
    # Add any other fields you need

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.first_name,self.last_name,self.mobile,self.username,self.email,self.dob)

