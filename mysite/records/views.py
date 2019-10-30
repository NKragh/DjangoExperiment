from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "index.html", {})