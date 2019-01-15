from django.urls import path

from . import views

urlpatterns = [
	path('login/', views.index, name='index'),
	path('logout/', views.log_out, name='log_out'),
	path('pass/', views.log_in, name='passs'),
    path('dash/', views.index2, name='index2'),
]