from django.contrib import admin

# Register your models here.

from . models import Portfolio, Teams

admin.site.register(Portfolio)
admin.site.register(Teams)
