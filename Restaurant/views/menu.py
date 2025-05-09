from django.shortcuts import render
from ..models import Dish

def menu_view(request):
    dishes = Dish.objects.all()

    # Фільтрація за категорією
    category = request.GET.get('category')
    if category:
        dishes = dishes.filter(category=category)

    # Фільтрація за вегетаріанством
    if request.GET.get('vegetarian') == 'on':
        dishes = dishes.filter(is_vegetarian=True)

    # Фільтрація за гостротою
    if request.GET.get('spicy') == 'on':
        dishes = dishes.filter(is_spicy=True)

    context = {'dishes': dishes}
    return render(request, 'menu.html', context)
