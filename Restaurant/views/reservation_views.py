from django.shortcuts import render
from django.views import View
from Restaurant.models import Reservation
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

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

@method_decorator(login_required(login_url='/admin/login/'), name='dispatch')
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class ReservationListView(View):
    template_name = 'reservation_list.html'

    def get(self, request):
        date_filter = request.GET.get('date')
        reservations = Reservation.objects.all()

        if date_filter:
            reservations = reservations.filter(reservation_date=date_filter)

        return render(request, self.template_name, {
            'reservations': reservations,
            'selected_date': date_filter
        })

    def post(self, request):
        cancel_id = request.POST.get('cancel_id')
        if cancel_id:
            Reservation.objects.filter(id=cancel_id).delete()
        return HttpResponseRedirect(reverse('reservation_list'))