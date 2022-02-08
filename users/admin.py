from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import KefirUser, City

# admin.site.register(KefirUser)


class KefirYserAdmin(UserAdmin):
    model = KefirUser


admin.site.register(City)
admin.site.register(KefirUser, KefirYserAdmin)