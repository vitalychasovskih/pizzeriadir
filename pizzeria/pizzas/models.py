from django.db import models

# Create your models here.


class Pizza(models.Model):
    """A simple attempt to create a pizza"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """returns a string representation of the model"""
        return self.name


class Topping(models.Model):
    """A topping for pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

# # Maybe I can not use it
#     class Meta:
#         verbose_name_plural = 'toppings'

    def __str__(self):
        """returns a string representation of the model"""
        return self.name
