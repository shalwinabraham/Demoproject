from django.urls import path,include
from .views import *

urlpatterns = [
        path('',register_view,name="register"),
        path('home/',home, name='home'),
]
