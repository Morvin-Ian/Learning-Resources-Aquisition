from django.urls import path
from DarajaApp.views import updatephone
from DarajaApp.Api.views import LnmApiGenericView



urlpatterns = [
    path('phone/',LnmApiGenericView.as_view(), name='generics'),
    path('phone/', updatephone,name='updatephone'),
    
  
]