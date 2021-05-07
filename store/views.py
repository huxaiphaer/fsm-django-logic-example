from django.shortcuts import render

# Create your views here.
from django_logic.exceptions import TransitionNotAllowed
from django_logic.process import logger
from rest_framework.response import Response
from rest_framework import generics

from store.models import Lock
from store.serializers import LockerSerializer


class LockerAPIView(generics.ListCreateAPIView):
    serializer_class = LockerSerializer

    def list(self, request, *args, **kwargs):
        query = Lock.objects.all()
        serializer = LockerSerializer(query, many=True)
        return Response(
            serializer.data
        )

    def create(self, request, *args, **kwargs):
        id = request.data['id']
        query = Lock.objects.get(id=id)
        try:
            # Change states from here e,g Am verifying an account
            query.process.action_verify_account()
            serializer = LockerSerializer(query)
            return Response(
                serializer.data
            )
        except TransitionNotAllowed:
            logger.error('Approve is not allowed')
            return Response(
                {'Transition not allowed'}
            )
