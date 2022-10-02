from django.db import models
from django import forms
from .models import Client, Invoice


class ClientForm(forms.ModelForm):
    class Meta():
        model = Client
        fields = "__all__"


class InvoiceForm(forms.ModelForm):
    class Meta():
        model = Invoice
        fields = "__all__"
