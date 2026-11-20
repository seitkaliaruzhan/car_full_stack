from rest_framework import serializers
from cars.models import Car, Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name']


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(), source='owner', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'color', 'registration_number', 'year', 'price', 'owner', 'owner_id']