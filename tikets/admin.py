from django.contrib import admin
from .models import Tiket


# Display models for admin site
class TiketAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject']

    class Meta:
        model = Tiket


# Register Models for admin site
admin.site.register(Tiket, TiketAdmin)
