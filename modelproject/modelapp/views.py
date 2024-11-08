from django.shortcuts import render,redirect
from .forms import BookingForm
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required



def bookings(request):
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Submitted")
        
    
    form = BookingForm()
    dict_form={

        'form': form
    }

    return render(request, 'booking.html' , dict_form)
   
# Create your views here.

@login_required()
def home(request):
    return render(request,'home.html')

from django.urls import reverse
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect

# -----------------loginpage--------------

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')


    form = CustomUserCreationForm()
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Registered Succesfully")
            return redirect(reverse('login'))
    return render(request, 'register.html',{'form':form})

@login_required()
def home(request):
    return render(request,'home.html')