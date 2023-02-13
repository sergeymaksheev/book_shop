from django.db import models
from catalog.models import Book
from orders.choises import ORDER_STATUS_CHOICES
from users.models import CustomUser
from django.core.validators import MinValueValidator


# Create your models here.
class Order(models.Model):
    """This class representing your order"""
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(
        choices=ORDER_STATUS_CHOICES,
        default='1',
        max_length=1,
    )
    is_paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"Order_{self.id}"


class OrderDetail(models.Model):
    """This class representing order detail"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None, related_name='order_detail')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    price_for_quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)


    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return f"Order detail_{self.id}"