from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    guests_number = models.PositiveIntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (f"Бронювання від {self.first_name} {self.last_name} "
                f"на {self.reservation_date} о {self.reservation_time}")
