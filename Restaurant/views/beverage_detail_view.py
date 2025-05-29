from Restaurant.models.beverage import Beverage
from django.shortcuts import render, get_object_or_404


def beverage_detail_view(request, slug):
    beverage = get_object_or_404(Beverage, slug=slug)
    return render(request, 'beverage_detail.html', {'beverage': beverage})