from django.shortcuts import render, redirect

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
        print account_info
        return redirect("/register")
