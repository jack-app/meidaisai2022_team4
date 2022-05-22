from calendar import week
from django.contrib import admin
from .models import Year, Month, Week, Event

admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Week)
admin.site.register(Event)