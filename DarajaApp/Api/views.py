from DarajaApp.models import LNMOnline
from .serializers import LNMOnlineSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
  
class LnmApiGenericView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]
   

    def create(self,request):
        print(request.data,"Successfull Morvin")

