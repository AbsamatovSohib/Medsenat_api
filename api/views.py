from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, pagination
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from api import models, serializer

# Create your views here.


class ApplySponsor(ListAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer
    pagination_class = None


class ListSponsor(ListAPIView):
    # s = sum(models.Donation.objects.filter(fromSponsor=1))

    queryset = models.Sponsor.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = [
        "title",
        "situation",
    ]
    serializer_class = serializer.SponsorListSerializer
    pagination_class = pagination.PageNumberPagination
    page_size = 10


class ListStudent(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer
    pagination_class = None


class StudentDetail(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer


class StudentUpdate(generics.UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer


class StudentCreate(generics.CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer


class SponsorDetail(generics.RetrieveAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer


class SponsorCreate(generics.CreateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer


class SponsorUpdate(generics.UpdateAPIView):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializer.SponsorSerializer
