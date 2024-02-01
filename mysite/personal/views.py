from django.shortcuts import render

def home_screen(request):
    print(request.headers)
    return render (request, 'base.html', {})

# Create your views here.
