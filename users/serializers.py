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

# "CurrentUserResponseModel": {
#                 "title": "CurrentUserResponseModel",
#                 "required": [
#                     "first_name",
#                     "last_name",
#                     "other_name",
#                     "email",
#                     "phone",
#                     "birthday",
#                     "is_admin",
#                 ],
#                 "type": "object",
#                 "properties": {
#                     "first_name": {"title": "First Name", "type": "string"},
#                     "last_name": {"title": "Last Name", "type": "string"},
#                     "other_name": {"title": "Other Name", "type": "string"},
#                     "email": {"title": "Email", "type": "string"},
#                     "phone": {"title": "Phone", "type": "string"},
#                     "birthday": {
#                         "title": "Birthday",
#                         "type": "string",
#                         "format": "date",
#                     },
#                     "is_admin": {"title": "Is Admin", "type": "boolean"},
#                 },
#             },