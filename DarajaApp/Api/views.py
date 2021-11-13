from DarajaApp.models import LNMOnline
from .serializers import LNMOnlineSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




  
class LnmApiGenericView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

  

    def create(self,request):
        print(request.data,"Successfull Morvin")

