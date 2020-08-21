from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    my_context = {
        "Name": "Terrence Moore",
        "Email": "tmm6907@gmail.com",
    }

    return render(request, "home.html", my_context)
