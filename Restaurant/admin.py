from django.contrib import admin
from .models import Category, Dish, Beverage, Reservation

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Beverage)
admin.site.register(Reservation)
