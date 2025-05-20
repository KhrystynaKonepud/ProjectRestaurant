import pytest
from django.urls import reverse
from Restaurant.models.dish import Dish
from Restaurant.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_dish_detail_view(client):
    cat = Category.objects.create(name="Гарячі страви", slug="hot")
    dish = Dish.objects.create(
        name="Паста",
        slug="pasta",
        price=145,
        weight=250,
        ingredients="Макарони, сир",
        category=cat,
        photo=SimpleUploadedFile("pasta.jpg", b"image content")
    )
    response = client.get(reverse('dish_detail', args=[dish.slug]))
    assert response.status_code == 200
    assert 'Паста' in response.content.decode('utf-8')
