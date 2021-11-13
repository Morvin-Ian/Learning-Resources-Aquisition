from django.urls import path
from . import views
from DarajaApp.Api.views import LnmApiGenericView



urlpatterns = [

    path('update/', views.updatephone,name='updatephone'),
    path('update/lnm/',LnmApiGenericView.as_view(), name='generics'),
  
]