from django import forms
from .models import Post

class RegisterPost(forms.ModelForm):
    title = forms.CharField(max_length=255, blank=False)
    content = forms.TextField()
    image = forms.ImageField(blank=True, null=True)