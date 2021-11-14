from django.urls import path
from DarajaApp.Api.views import LnmApiGenericView
from DarajaApp.views import updatephone



urlpatterns = [

    path('lnm/',LnmApiGenericView.as_view(), name='generics'),
    path('phone/',LnmApiGenericView.as_view(), name='phone'),
    
  
]