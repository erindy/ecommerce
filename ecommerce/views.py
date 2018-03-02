from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm


def home_page(request):
    return render(request, "home_page.html")

def about_page(request):
    return render(request, "home_page.html")


def contact_page(request):

    if request.method == "POST":
        print(request.POST.get('fullname'))
    context = {
        'title': "Contact",
        "content": "Welcome to the contact page."
    }
    return render(request, "contact/view.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/login.html", {})

def register_page(request):
    return render(request, "auth/login.html", {})


