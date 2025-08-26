from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ["category","title","description"]
class AdminServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields=["category","title","description","status"]
