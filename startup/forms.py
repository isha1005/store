from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100, required=True)
    email = forms.EmailField()
    company_name = forms.CharField(required=False)
    notes = forms.CharField(max_length=400, required=False)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'company_name', 'notes']
