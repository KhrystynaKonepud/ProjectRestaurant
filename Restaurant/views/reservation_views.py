from django.shortcuts import render
from django.views import View
from Restaurant.models import Reservation
from django.utils import timezone

class ReservationView(View):
    template_name = 'reservation_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = request.POST

        Reservation.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            phone=data.get('phone'),
            guests_number=data.get('guests_number'),
            reservation_date=data.get('reservation_date'),
            reservation_time=data.get('reservation_time'),
            details=data.get('details'),
            created_at=timezone.now()
        )

        return render(request, self.template_name, {
            'success': True
        })
