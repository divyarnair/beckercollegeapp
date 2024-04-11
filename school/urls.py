from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('signin', views.signin, name="signin"),
    path('login',views.login,name='login'),
    path('click',views.click,name='click'),
    path('form',views.form,name='form'),
    path('submitted',views.submitted,name='submitted'),
    path('logout',views.logout,name='logout'),
    path('homepage',views.homepage,name='homepage'),

]