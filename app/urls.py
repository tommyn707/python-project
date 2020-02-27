from django.urls import path
from . import views

urlpatterns = [
		path('', views.index),
        path('register', views.reg_page),
        path('homepage', views.homepage,),
        path('logout', views.logout),
]