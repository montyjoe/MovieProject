from django.shortcuts import render, redirect
from . import services
from ..User_app.models import User, Profile, Movie, Friend
from ..User_app import views


# Create your views here.
"""

api key = 286abf6056d0a1338f772d1b7202e728
"""
def index(request):
    result = services.get_discover()
    if "user" in request.session :
        status = 'You are logged in'
        users = User.objects.exclude(id= request.session['user']).order_by('-created_at')
        friend, created = Friend.objects.get_or_create(current_user=User.objects.get(id = request.session['user']))
        friends = friend.users.all()
        return render(request, 'homeApp/index.html', {'status': status, 'result': result, 'users': users, 'friends': friends})

    else:
        status = "You are NOT logged in"
        users = User.objects.all().order_by('-created_at')
        return render(request, 'homeApp/index.html', {'status': status, 'result': result, 'users': users})




def testing(request):
    return redirect('/')
