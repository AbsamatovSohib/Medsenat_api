from django.shortcuts import render
from api import models
from rest_framework.generics import ListAPIView
from api import serializer
# Create your views here.

class ApplySponsor(ListAPIView):

    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer
    pagination_class = None