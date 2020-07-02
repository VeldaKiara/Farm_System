from django.contrib import admin

# Register your models here.
from products.models import Food, Fertilizer, Pesticide, Machinery, Tools

admin.site.register(Food)
admin.site.register(Fertilizer)
admin.site.register(Pesticide)
admin.site.register(Machinery)
admin.site.register(Tools)