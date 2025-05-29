import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view_status_code(client):
    """Перевірка, що головна сторінка доступна."""
    url = reverse('home')  # переконайся, що в urls.py є path('', home_view, name='home')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_home_view_template_used(client):
    """Перевірка, що використовується правильний шаблон."""
    response = client.get(reverse('home'))
    assert 'home.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_home_view_contains_header(client):
    """Перевірка, що на сторінці є логотип і кнопка."""
    response = client.get(reverse('home'))
    content = response.content.decode('utf-8')
    assert '<img' in content
    assert 'Забронювати столик' in content

@pytest.mark.django_db
def test_home_view_contains_text_block(client):
    """Перевірка, що на сторінці є текст привітання."""
    response = client.get(reverse('home'))
    content = response.content.decode('utf-8')
    assert 'Ласкаво просимо до Oishii' in content
    assert 'Ми готуємо страви з різних куточків Азії' in content

@pytest.mark.django_db
def test_footer_always_visible(client):
    """Перевірка, що футер присутній на сторінці."""
    response = client.get(reverse('home'))
    content = response.content.decode('utf-8')
    assert 'Усі права захищені' in content
