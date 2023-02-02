from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
'''class UserProfile(models.Model):
    """This class representing information about users"""
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, help_text="Users's phone")
    email = models.EmailField(help_text="User's email")
    discount = models.IntegerField(help_text="Personal discount", default=0)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.user'''

class CustomUser(AbstractUser):
    
    def __str__(self) -> str:
        return self.username