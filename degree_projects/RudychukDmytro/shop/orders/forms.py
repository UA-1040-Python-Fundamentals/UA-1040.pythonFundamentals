from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    phone = forms.CharField(max_length=17)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=30)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city',]