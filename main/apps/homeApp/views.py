from django.shortcuts import render, redirect
from . import services



# Create your views here.
"""

api key = 286abf6056d0a1338f772d1b7202e728
"""
def index(request):
    if "user" in request.session :
        status = 'You are logged in'
    else:
        status = "You are NOT logged in"

    result = services.get_discover()
    return render(request, 'homeApp/index.html', {'status': status, 'result': result})


def testing(request):
    return redirect('/')
