from rest_framework import serializers

from .models import Clients, Users

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'company_name')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'last_name', 'first_name', 'username', 'role', 'phone', 'address', 'client_id')