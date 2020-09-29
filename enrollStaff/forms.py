from django import forms
from .models import CreateStaff


class StaffRegistration(forms.ModelForm):
    class Meta:
        model = CreateStaff
        fields = ['name', 'email', 'staffType', 'age', 'gender', 'password']
