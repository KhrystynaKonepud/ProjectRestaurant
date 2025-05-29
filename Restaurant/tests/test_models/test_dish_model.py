import pytest
from Restaurant.models.dish import Dish
from Restaurant.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_dish_str():
    cat = Category.objects.create(name="Салати", slug="salaty")
    dish = Dish.objects.create(
        name="Цезар",
        slug="cezar",
        price=180,
        weight=250,
        ingredients="Курка, салат, пармезан",
        category=cat,
        photo=SimpleUploadedFile("dish.jpg", b"image content")
    )
    assert str(dish) == "Цезар"
