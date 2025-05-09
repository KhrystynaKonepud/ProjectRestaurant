from django.db import models

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Закуска'),
        ('main', 'Основна страва'),
        ('dessert', 'Десерт'),
        ('drink', 'Напій'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    cuisine_type = models.CharField(max_length=50, default='Азіатська')

    def __str__(self):
        return self.name
