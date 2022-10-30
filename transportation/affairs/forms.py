from .models import CourierModel, CustomerModel
from django import forms

class CourierForm(forms.ModelForm):
    class Meta:
        model = CourierModel
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = '__all__'