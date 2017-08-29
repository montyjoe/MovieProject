from django.shortcuts import render, redirect, HttpResponse
from . import services
from ..User_app.models import User, Profile, Movie, Friend
from ..User_app import views
from django.views.generic.edit import FormView
import json



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
        try:
            profile = Profile.objects.filter(user_id=User.objects.get(id=request.session['user']))
        except:
            pass
        return render(request, 'homeApp/index.html', {'status': status, 'result': result, 'users': users, 'friends': friends, 'profile': profile})

    else:
        status = "You are NOT logged in"
        users = User.objects.all().order_by('-created_at')
        return render(request, 'homeApp/index.html', {'status': status, 'result': result, 'users': users})




def testing(request):
    return redirect('/')




def get_places(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        users = User.objects.filter(first_name__icontains = q )[:20]
        results = []
        for user in users:
            user_json = {}
            user_json['id'] = user.id
            user_json['label'] = user.first_name
            user_json['value'] = user.first_name
            results.append(user_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    print data
    return HttpResponse(data, mimetype)

def search(request):
    if request.method == 'POST':
        count = User.objects.filter(first_name__icontains=request.POST['person']).count()
        users = User.objects.filter(first_name__icontains=request.POST['person'])
        print users
        return render(request, 'homeApp/search.html', {'users' : users, 'count' : count})

# def get_places(request):
#   if request.is_ajax():
#     q = request.GET.get('term', '')
#     users = User.objects.filter(first_name__icontains=q)
#     results = []
#     for user in users:
#       user_json = {}
#       user_json['id'] = user.id
#       user_json['label'] = user.first_name
#       user_json['value'] = user.first_name
#       results.append(user_json)
#     data = json.dumps(results)
#   else:
#     data = 'fail'
#   mimetype = 'application/json'
#   return HttpResponse(data, mimetype)


# class AutoCompleteView(FormView):
#     def get(self,request,*args,**kwargs):
#         data = request.GET
#         username = data.get("term")
#         if username:
#             users = User.objects.get(username__icontains = username)
#         else:
#             users = User.objects.all()
#         results = []
#         for user in users:
#             user_json = {}
            # user_json['id'] = user.id
            # user_json['label'] = user.first_name
            # user_json['value'] = user.first_name
#             results.append(user_json)
#             data = json.dumps(results)
#             mimetype = 'application/json'
#             return HttpResponse(data, mimetype)
