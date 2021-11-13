from django.urls import path
from DarajaApp.Api.views import LnmApiGenericView



urlpatterns = [

    path('lnm/',LnmApiGenericView.as_view(), name='generics'),
  
]