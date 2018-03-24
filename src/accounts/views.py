from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

from django.shortcuts import render, redirect
from .forms import UserLoginForm
from schoolmanagement.models import School


# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        try:
            user = authenticate(username=username, password=password)
            login(request, user) 
        except:
            print("invalid user") 
        # print("logged in ", request.user.is_authenticated)
        user = request.user
        school = user.schoolid
        #redirect
        return redirect(user)
    return render(request, "form.html", {"form": form, })

def logout_view(request):
    logout(request)
    return redirect(login_view)
