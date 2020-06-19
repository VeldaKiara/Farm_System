from django.contrib import admin

# Register your models here.
from accounts.models import Products, Fertilizer, Pesticide, Machinery, Tools

admin.site.register(Products)
admin.site.register(Fertilizer)
admin.site.register(Pesticide)
admin.site.register(Machinery)
admin.site.register(Tools)