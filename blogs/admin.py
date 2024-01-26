from django.contrib import admin

# Register your models here.

from .models import Blog, Lawyer

admin.site.register(Blog)
admin.site.register(Lawyer)
