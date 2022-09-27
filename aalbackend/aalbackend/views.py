from rest_framework import viewsets

from .serializers import UsersSerializer
from .serializers import ClientsSerializer
from .models import Clients, Users

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all().order_by('ID')
    serializer_class = ClientsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('ROLE')
    serializer_class = UsersSerializer