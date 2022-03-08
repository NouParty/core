from rest_framework import serializers

from .models import SellerModel


class SellerSerializer(serializers.ModelSerializer):
    model = SellerModel
    fields = "__all__"
