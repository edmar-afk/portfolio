from django.contrib import admin
from .models import Products, Comments, Counter


admin.site.register(Counter)
admin.site.register(Products)
admin.site.register(Comments)