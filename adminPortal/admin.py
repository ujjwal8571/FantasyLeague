from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(AdminUser)
admin.site.register(Player)
admin.site.register(PlayerScore)
