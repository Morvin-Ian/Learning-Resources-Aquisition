from django.urls import path
from .views import LNM
from . import views



urlpatterns = [

    path('lnm/',LNM.as_view(), name='lnm'),
    path('phone/<int:id>', views.updatephone, name='phone')
  
  
]