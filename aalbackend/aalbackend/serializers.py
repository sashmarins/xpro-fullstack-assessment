from rest_framework import serializers

from .models import Clients, Users

class ClientsSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('ID, COMPANY_NAME')

class UsersSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('ID, LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID')