from .models import Covers
from rest_framework import serializers


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covers
        fields = '__all__'

    def validate(self, data):
        return super(CoverSerializer, self).validate(data)

    def create(self, validated_data):
        instance = Covers.objects.create(**validated_data)
        return instance
