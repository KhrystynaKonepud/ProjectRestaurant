import pytest
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from Restaurant.models import Reservation

@pytest.fixture
def staff_user(db):
    user = User.objects.create_user(username='admin', password='1234', is_staff=True)
    return user

@pytest.fixture
def valid_data():
    return {
        'first_name': 'Юлія',
        'last_name': 'Кнап',
        'phone': '0673563763',
        'guests_number': 2,
        'reservation_date': (timezone.now() + timedelta(days=1)).date().isoformat(),
        'reservation_time': '18:30',
        'details': 'Столик біля вікна'
    }

@pytest.mark.django_db
def test_get_reservation_form(client):
    url = reverse('reservation')
    response = client.get(url)
    assert response.status_code == 200
    assert 'reservation_form.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_post_valid_reservation(client, valid_data):
    url = reverse('reservation')
    response = client.post(url, data=valid_data)
    assert response.status_code == 200
    assert Reservation.objects.filter(first_name='Юлія').exists()
    assert 'Ваше бронювання створено' in response.content.decode()

@pytest.mark.django_db
def test_reservation_list_as_staff(client, staff_user, valid_data):
    client.login(username='admin', password='1234')
    Reservation.objects.create(**valid_data)
    url = reverse('reservation_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Юлія' in response.content.decode()

@pytest.mark.django_db
def test_reservation_list_filter_by_date(client, staff_user, valid_data):
    client.login(username='admin', password='1234')
    Reservation.objects.create(**valid_data)
    url = reverse('reservation_list')
    filter_date = valid_data['reservation_date']
    response = client.get(url, {'date': filter_date})
    assert response.status_code == 200
    assert filter_date in response.content.decode()

@pytest.mark.django_db
def test_cancel_reservation(client, staff_user, valid_data):
    client.login(username='admin', password='1234')
    reservation = Reservation.objects.create(**valid_data)
    url = reverse('reservation_list')
    response = client.post(url, {'cancel_id': reservation.id}, follow=True)
    assert response.status_code == 200
    assert not Reservation.objects.filter(id=reservation.id).exists()