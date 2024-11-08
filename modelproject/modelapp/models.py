from django.db import models

class Booking(models.Model):
    p_name=models.CharField(max_length=50)
    p_number=models.IntegerField()
    p_email=models.EmailField()
    booking_date= models.DateField()
    booking_on=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.p_name