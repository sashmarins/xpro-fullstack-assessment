from crypt import methods
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404
from django.db.models import Value as V
from django.db.models.functions import Concat

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
        for user in queryset:
            if (user.client_id == int(self.request.data.get('client_id'))):
                usersList.append(user)
        serializer = serializers.UsersSerializer(usersList, many=True)
        data = serializer.data
        return Response(data)
    @action(detail = False, methods=['post'], url_path="search")
    def search(self, args):
        usersList = []
        query = self.request.data.get('UserSearch')
        firstnameqs = Users.objects.filter(first_name__icontains=query)
        usernameqs = Users.objects.filter(username__icontains=query)
        # emailqs = Users.objects.filter(email__icontains=query)
        if firstnameqs:
            for user in firstnameqs:
                usersList.append(user)
        if usernameqs:
            for user in usernameqs:
                usersList.append(user)
        serializer = serializers.UsersSerializer(usersList, many=True)
        print("user list",usersList)
        data = serializer.data
        if Response(data) == []:
            return Http404
        return Response(data)
    @action(detail = False, methods=['post'], url_path="login")
    def login(self, args):
        qs = (Users.objects.all())
        for user in qs:
            if (user.username == (self.request.data.get('username'))):
                serializer = serializers.UsersSerializer(user)
                data = serializer.data
                return Response(data)
        # return Http404
        # no user with a match was found
