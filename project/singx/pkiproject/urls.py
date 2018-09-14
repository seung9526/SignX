from django.urls import path, include

from . import views

app_name = 'pkiproject'

urlpatterns = [
	path('', views.index, name = 'index'),
    path('join/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('car/', views.car_form, name='car_form'),
]