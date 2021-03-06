from rest_framework import serializers

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name", "city", "street", "street_number")
