from django.db import models
from Restaurant.models.category import Category


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.TextField()
    photo = models.ImageField(upload_to='dishes/')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    sort = models.PositiveIntegerField(default=0)
    is_vegetarian = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    cuisine_type = models.CharField(max_length=50, default='Азіатська')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort']
        db_table = 'dish'

    def __str__(self):
        return self.name

