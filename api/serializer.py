from rest_framework import serializers

from . import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = ["title", "phone", "person_type", "money"]


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        exclude = ["person_type"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"
