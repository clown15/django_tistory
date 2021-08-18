from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    # HTML에서 input type을 설정하기 위해 widget사용
    password = CharField(label="비밀번호", widget=forms.PasswordInput)
    confirm_password = CharField(label="비밀번호 확인", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','name','gender','email']

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

        return cd['confirm_password']