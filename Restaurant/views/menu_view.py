from django.shortcuts import render, get_object_or_404
from Restaurant.models.dish import Dish
from Restaurant.models.beverage import Beverage
from Restaurant.models.category import Category


def menu_view(request, category_slug=None):
    categories = Category.objects.filter(is_visible=True).order_by('sort')

    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        dishes = Dish.objects.filter(is_visible=True, category=selected_category).order_by('sort')
        beverages = Beverage.objects.filter(is_visible=True, category=selected_category).order_by('sort')
    else:
        selected_category = None
        dishes = Dish.objects.filter(is_visible=True).order_by('sort')
        beverages = Beverage.objects.filter(is_visible=True).order_by('sort')

    context = {
        'categories': categories,
        'selected_category': selected_category,
        'dishes': dishes,
        'beverages': beverages
    }
    return render(request, 'menu.html', context)


