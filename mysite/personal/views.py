from django.shortcuts import render

def home_screen(request):
    # context = {}
    # Way One of using variables
    # context['some_text'] = "This is some Important Text"
    # context['some_number'] = 123456

    # Method Two of Using Variables

    context = {
        "some_text": "This is some Important Text",
        "some_number": 123456,
    }


    return render (request, 'personal/home.html', context)

# Create your views here.
