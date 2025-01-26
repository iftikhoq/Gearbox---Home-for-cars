from django.contrib import admin

from .models import Orders, CustomUser

admin.site.register(Orders)
admin.site.register(CustomUser)