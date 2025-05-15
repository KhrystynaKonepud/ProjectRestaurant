from django.db import models
from Restaurant.models.category import Category


class Beverage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    volume = models.DecimalField(max_digits=6, decimal_places=2)
    is_alcoholic = models.BooleanField(default=False)
    ingredients = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='beverages/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sort = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort']
        db_table = 'beverage'

    def __str__(self):
        return self.name
