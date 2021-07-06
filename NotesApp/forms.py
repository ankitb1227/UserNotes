from django import forms
from .models import Attachment


class Userform(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = '__all__'
