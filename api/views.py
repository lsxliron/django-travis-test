# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Person


class PersonViewSet(ViewSet):

    def get(self, request, uuid):
        try:
            person = Person.objects.get(uuid=uuid)
        except ValidationError:
            return Response({"status": "error", "reason": "Invalid UUID"}, status=status.HTTP_400_BAD_REQUEST)

        except Person.DoesNotExist:
            return Response({"status": "error", "reason": "UUID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({'status': 'ok', 'uuid': obj.uuid}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'reason': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def patch(self, request, uuid):
        try:
            person = Person.objects.get(uuid=uuid)
        except ValidationError:
            return Response({"status": "error", "reason": "Invalid UUID"}, status=status.HTTP_400_BAD_REQUEST)

        except Person.DoesNotExist:
            return Response({"status": "error", "reason": "UUID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'reason': serializer.errors}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            person = Person.objects.get(uuid=uuid)
        except ValidationError:
            return Response({"status": "error", "reason": "Invalid UUID"}, status=status.HTTP_400_BAD_REQUEST)

        except Person.DoesNotExist:
            return Response({"status": "error", "reason": "UUID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response({"status": "ok"})
