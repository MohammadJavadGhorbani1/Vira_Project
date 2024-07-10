from django.shortcuts import render
from django.views import *

# Create your views here.

class HomePage(View):
    def get(self , request):
        return render(request , 'home.html' , {

        })

def header_render_partial(request):
    return render(request , 'header.html' , {

    })

def footer_render_partial(request):
    return render(request , 'footer.html' , {

    })
