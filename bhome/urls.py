from django.contrib import admin
from django.urls import path
from bhome import views

'''
All important urls for routing are written here
'''

urlpatterns = [
    path('', views.home, name='home'),
    path('listings', views.listings, name='listings'),
    path('owners', views.owners, name='owners'),
    path('services', views.services, name='services'),
    path('house/<str:pk>', views.house, name='house'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
]
