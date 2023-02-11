from django.db import models
from catalog.models import TheRestOfTheBook, Book
from users.models import CustomUser
from django.core.validators import MinValueValidator


# Create your models here.
class Order(models.Model):
    """This class representing your order"""
    user_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=100, default=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"Order_{self.id}"


class OrderDetail(models.Model):
    """This class representing order detail"""

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(TheRestOfTheBook, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    total_price = models.IntegerField(validators=[MinValueValidator(0)])

    

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"Order detail_{self.id}"