from django.contrib import admin
from .models import Usuario


class User(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(Usuario,User)