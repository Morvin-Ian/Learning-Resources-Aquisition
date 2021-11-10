from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home-page'),
    path('register/',views.register,name='register'),
  
]