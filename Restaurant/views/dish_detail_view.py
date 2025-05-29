from django.shortcuts import render, get_object_or_404
from Restaurant.models.dish import Dish


def dish_detail_view(request, slug):
    dish = get_object_or_404(Dish, slug=slug)
    return render(request, 'dish_detail.html', {'dish': dish})