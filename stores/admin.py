from django.contrib import admin

from stores import models


class StoreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'name', 'city', 'street', 'street_number'
    )


admin.site.register(models.Store, StoreAdmin)
