from django.contrib import admin

from users.models import KefirUser, City


class KefirUserAdmin(admin.ModelAdmin):
    model = KefirUser


admin.site.register(City)
admin.site.register(KefirUser, KefirUserAdmin)
