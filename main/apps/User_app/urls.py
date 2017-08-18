from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login_page),
    url(r'^register$', views.register_page),
    url(r'^register_account$', views.register_account),

]
