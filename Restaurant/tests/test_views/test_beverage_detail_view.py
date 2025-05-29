import pytest
from django.urls import reverse
from Restaurant.models.beverage import Beverage
from Restaurant.models.category import Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_beverage_detail_view(client):
    cat = Category.objects.create(name="Напої", slug="drinks")
    bev = Beverage.objects.create(
        name="Мохіто",
        slug="mohito",
        price=60,
        volume=250,
        is_alcoholic=True,
        category=cat,
        photo=SimpleUploadedFile("mojito.jpg", b"image content")
    )
    response = client.get(reverse('beverage_detail', args=[bev.slug]))
    assert response.status_code == 200
    assert 'Мохіто' in response.content.decode('utf-8')
