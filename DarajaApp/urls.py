from django.urls import path
from .views import LnmApiGenericView
from . import views



urlpatterns = [

    path('lnm/',LnmApiGenericView.as_view(), name='generics'),
    path('phone/<int:id>', views.updatephone, name='phone')
  
  
]