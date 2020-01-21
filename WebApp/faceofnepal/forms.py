from django import forms
from faceofnepal.models import Freelancer
#DataFlair
class FreelancerCreate(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'