from django.shortcuts import render, redirect
from .models import User

# Create your views here.
# =================================================================
# template renders
# =================================================================
def login_page(request): #renders the login page template
    return render(request, 'User_app/login_page.html')

def register_page(request): #renders the register page template
    return render(request, 'User_app/register_page.html')



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
            return redirect('/')
        else:
            print result['errors']
            return redirect("/register")


def log_user_in(request):
    if request.method == 'POST':
        login_info = {
            "email": request.POST['email'],
            "password": request.POST['password']
        }

        result = User.objects.login(login_info)

        if result['errors'] == None:
            request.session['id'] = result['user'].id
            return redirect('/')
        else:
            print result['errors']
            return redirect('/login')
























# end
