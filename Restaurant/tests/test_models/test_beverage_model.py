import pytest
from Restaurant.models.beverage import Beverage
from Restaurant.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_beverage_str():
    cat = Category.objects.create(name="Напої", slug="napoi")
    bev = Beverage.objects.create(
        name="Лимонад",
        slug="lemonade",
        price=55,
        volume=300,
        is_alcoholic=False,
        category=cat,
        photo=SimpleUploadedFile("bev.jpg", b"image content")
    )
    assert str(bev) == "Лимонад"
