from django.shortcuts import render
from django.http import HttpResponse
from records.models import Record

# Create your views here.
def index(request):
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "index.html", {})

def tutorial_view(request):
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": ["a", "b", "c", "d"]
    }
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "about.html", my_context)

def contact_view(request):
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "contact.html", {})

def record_detail_view(request):
    obj = Record.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'artist': obj.artist, 
    #     'duration': obj.duration,
    #     'yearOfPublication': obj.yearOfPublication
    # }
    context = {
        "object": obj
    }
    return render(request, "record/detail.html", context)