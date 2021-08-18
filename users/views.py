from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # DB에 저장하지 않음
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return request(request,)
