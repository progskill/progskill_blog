from django.shortcuts import render

def home_screen(request):
    print(request.headers)
    # Passing Variables -  Method 1


   # Passing Variables -  Method 2



    # Passing a list of variables


    return render (request, 'personal/home.html', {})