from myapp.models import Person
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class PersonSerializer(ModelSerializer):
    first_name = serializers.CharField(source='fname')
    last_name = serializers.CharField(source='lname')

    class Meta:
        fields = ('first_name', 'last_name', 'age')
        model = Person
