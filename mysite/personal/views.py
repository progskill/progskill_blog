from django.shortcuts import render

def home_screen(request):
    print(request.headers)
    return render (request, 'personal/home.html', {})

# Create your views here.
