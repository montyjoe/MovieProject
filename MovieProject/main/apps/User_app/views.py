from django.shortcuts import render, redirect
from .models import User, Profile, Movie, Friend
from django.core.urlresolvers import reverse

"""
things that need to be added?
1. validation messages
2. make sure that password is protected using Bcrpt and confirm password

"""
# Create your views here.
# =================================================================
# template renders
# =================================================================
def login_page(request): #renders the login page template
    return render(request, 'User_app/login_page.html')

def register_page(request): #renders the register page template
    return render(request, 'User_app/register_page.html')

def profile(request):
    if 'user' not in request.session:
        return redirect('/login')
    username = request.session['name']
    profile = Profile.objects.filter(user_id = User.objects.get(id = request.session['user']))
    context = {
    'profile' : profile,
    'username' : username
    }
    print request.session['user']
    return render(request, "User_app/profile.html", context)

# =================================================================
# POST request's
# =================================================================
def register_account(request): #this function creates the account
    if request.method == 'POST':
        account_info = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            "email": request.POST['email'],
            "password": request.POST['password']
        }
        result = User.objects.register(account_info)
        if result['errors'] == None:
            request.session['name'] = result['user'].first_name
            request.session['user'] = result['user'].id
            request.session['action'] = "registered"
            return redirect('/')
        else:
            print result['errors']
            return redirect("/register")


def log_user_in(request): # this is to the log the user in
    if request.method == 'POST':
        login_info = {
            "email": request.POST['email'],
            "password": request.POST['password']
        }

        result = User.objects.login(login_info)

        if result['errors'] == None:
            request.session['email'] = result['user'].email
            request.session['name'] = result['user'].first_name
            request.session['user'] = result['user'].id
            request.session['action'] = "logged in"
            return redirect('/')
        else:
            print result['errors']
            return redirect('/login')


def createProfile(request):
    if request.method == 'POST':
        profile = Profile.objects.create(
            birthday = request.POST['birthday'],
            hometown = request.POST['hometown'],
            country = request.POST['country'],
            user_id = User.objects.get(id = request.session['user'])
        )
    return redirect('/profile')

# renders the specific user page, other than the current user

def user_page(request, id):
    context = {
    'users' : User.objects.filter(id = id),
    'profile' : Profile.objects.get(user_id=id)
    }
    return render(request, 'User_app/user.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


# function that calls on the Friend Methods to add or remove a friend

def change_friends(request, operation, pk):
    new_friend = User.objects.get(id=pk)
    if operation == 'add':
        Friend.add_friend(User.objects.get(id=request.session['user']), new_friend)
    elif operation == 'remove':
        Friend.lose_friend(User.objects.get(id=request.session['user']), new_friend)

    return redirect('/')

























# end
