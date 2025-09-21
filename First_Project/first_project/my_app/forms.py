from django import forms
from .models import Sing_up


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class SingupForm(forms.Form):
    
    class Meta:
        model = Sing_up
        fields = ['name', 'email', 'message']
