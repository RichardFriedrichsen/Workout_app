from django.contrib import admin

# Register your models here.

from .models import exercise, workout

admin.site.register(exercise)
admin.site.register(workout)