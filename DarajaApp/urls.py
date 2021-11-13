from django.urls import path
from . import views
from .views import MpesaApiView

urlpatterns = [
 
    path('lnm/<int:id>',MpesaApiView.as_view(), name='api'),
    path('update/<int:id>', views.updatephone,name='updatephone')
  
]