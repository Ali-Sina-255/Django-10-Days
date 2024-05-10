from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register', views.register_view, name='register'),
]
