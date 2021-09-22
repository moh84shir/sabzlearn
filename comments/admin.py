from django.contrib import admin
from . import models


# Register models.
admin.site.register(models.Comment)
admin.site.register(models.Replay)
