from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')
