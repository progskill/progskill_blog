from django.shortcuts import render

def home_screen(request):
    context = {}
    # Way One of using variables
    context['some_text'] = "This is some Important Text"
    context['some_number'] = 123456

    # Method Two of Using Variables

    return render (request, 'personal/home.html', context)

# Create your views here.
