from rest_framework import serializers

from users.models import KefirUser, City


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


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
    id = serializers.IntegerField(source="pk")

    class Meta:
        model = KefirUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]


class KefirAdminUserListSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=True)

    class Meta:
        model = KefirUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "city"
        ]
        depth = 1

    def create(self, validated_data):
        city_data = validated_data.pop("city")
        kefir_user = KefirUser.objects.create(**validated_data)
        for city in city_data:
            city = City.objects.get_or_create(**dict(city))[0]
            kefir_user.city.add(city)
        return kefir_user


class KefirUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = KefirUser
        fields = [
            "first_name",
            "last_name",
            "other_name",
            "email",
            "phone",
            "birthday",
        ]
