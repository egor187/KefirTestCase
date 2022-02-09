from rest_framework import serializers
from users.models import KefirUser, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("name",)


class KefirUserSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = KefirUser
        fields = [
            "first_name",
            "last_name",
            "other_name",
            "email",
            "phone",
            "birthday",
            "is_admin",
            "city"
        ]


class KefirUserListSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    id = serializers.IntegerField(source="pk")

    class Meta:
        model = KefirUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "city"
        ]
