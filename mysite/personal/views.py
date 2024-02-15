from django.shortcuts import render

def home_screen(request):
    context = {}
    # Way One of using variables
    # context['some_text'] = "This is some Important Text"
    # context['some_number'] = 123456

    # Method Two of Using Variables

    # context = {
    #     "some_text": "This is some Important Text",
    #     "some_number": 123456,
    # }


    # Passing a list of variables

    list_variables = []
    list_variables.append("Value 1")
    list_variables.append("Value 2")
    list_variables.append("Value 3")
    list_variables.append("Value 4")
    context['variable_list']  = list_variables


    return render (request, 'personal/home.html', context)

# Create your views here.
