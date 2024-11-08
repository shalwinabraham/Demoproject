from django import forms
from .models import Booking

class Dateinput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : Dateinput()
        }


        labels = {

            'p_name' : 'patient name',
            'p_number': 'patient phone',
            'p_email':'patient email',
    }


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

        