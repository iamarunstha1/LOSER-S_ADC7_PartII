from django import forms
from .models import Freelancer
class FreelancerForms(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = "__all__"