from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Home",
        "content": "Home - furniture shop"
    }
    return render(request=request, template_name="main/index.html", context=context)

def about(request):
    context = {
        "title": "About us",
        "content": "Home - about us",
        "text_on_page": "Hello world! My name is Andrii and I am from Ukraine and it is my Home shop!"
    }

    return render(request=request, template_name="main/about.html", context=context)
