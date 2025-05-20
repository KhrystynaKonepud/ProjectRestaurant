import pytest
from datetime import date, time
from Restaurant.models.reservation import Reservation

@pytest.mark.django_db
def test_reservation_str():
    res = Reservation.objects.create(
        first_name="Анна",
        last_name="Іванова",
        phone="0931112233",
        guests_number=2,
        reservation_date=date(2025, 5, 25),
        reservation_time=time(18, 0)
    )
    assert "Анна Іванова" in str(res)
    assert "2025" in str(res)
