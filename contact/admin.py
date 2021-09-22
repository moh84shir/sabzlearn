from django.contrib import admin
from .models import Contact


# Display contact models for admin site
class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'user', 'email', 'is_read']

    class Meta:
        model = Contact


# Register models.
admin.site.register(Contact, ContactAdmin)
