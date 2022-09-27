from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404

from .serializers import UsersSerializer
from .serializers import ClientsSerializer
from .models import Clients, Users
from aalbackend import serializers

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all().order_by('id')
    serializer_class = ClientsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('role', 'id')
    serializer_class = UsersSerializer
    @action(detail = False, methods=['post'], url_path = "byClient")
    def byClient(self, args):
        usersList = []
        queryset = (Users.objects.all())
        print(queryset)
        for user in queryset:
            print(user.client_id)
            print("request", self.request.data.get('client_id'))
            if (user.client_id == int(self.request.data.get('client_id'))):
                print("appended user")
                usersList.append(user)
        serializer = serializers.UsersSerializer(usersList, many=True)
        data = serializer.data
        return Response(data)
