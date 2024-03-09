from django.shortcuts import render, HttpResponse


def contactus(request):
    return HttpResponse('09121121212')


def home(request):
    return render(request, "home_app/home.html")