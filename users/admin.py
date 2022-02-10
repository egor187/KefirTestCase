from django.contrib import admin
from .models import KefirUser, City


class KefirUserAdmin(admin.ModelAdmin):
    model = KefirUser


admin.site.register(City)
admin.site.register(KefirUser, KefirUserAdmin)
