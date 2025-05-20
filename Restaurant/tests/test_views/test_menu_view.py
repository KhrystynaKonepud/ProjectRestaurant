import pytest
from django.urls import reverse
from Restaurant.models.category import Category

@pytest.mark.django_db
def test_menu_view(client):
    response = client.get(reverse('menu'))
    assert response.status_code == 200
    assert 'Меню' in response.content.decode('utf-8')
