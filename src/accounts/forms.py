from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            print(username + password)
            raise forms.ValidationError("This user does not exists")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")
        if not user.is_active:
            raise forms.ValidationError("User is no longer active")
        return super(UserLoginForm, self).clean()
