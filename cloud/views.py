from django.shortcuts import render
from django.conf import settings


# Create your views here.

def home(request):
    context = {
        "title": "eLearning",
    }

    return render(request, "home.html", context)
