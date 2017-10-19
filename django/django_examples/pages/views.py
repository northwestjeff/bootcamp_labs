from django.shortcuts import render, HttpResponse

def home(request):
    name = "Jeff"
    return render(request, 'pages/home.html', {"name": name})


def about(request):
    return render(request, 'pages/about.html', {})