from django.shortcuts import render

def home_screen(request):
    print(request.headers)
    # Passing Variables -  Method 1
    context = {}
    # context['some_string'] = "Hello world, this is some awesome"
    # context['some_num'] = 12345

   # Passing Variables -  Method 2

    # context = {
    #     "some_string": "Hello world, this is some awesome 2",
    #     "some_num": 123453434534545
    # }



    # Passing a list of variables

    list_varaibles = []
    list_varaibles.append("Value 1")
    list_varaibles.append("Value 2")
    list_varaibles.append("Value 3")
    context["list_varaibles"] = list_varaibles


    return render (request, 'personal/home.html', context)