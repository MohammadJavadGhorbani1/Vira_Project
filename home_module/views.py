from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request , 'home.html' , {

    })

def header_render_partial(request):
    return render(request , 'header.html' , {

    })

def footer_render_partial(request):
    return render(request , 'footer.html' , {

    })
