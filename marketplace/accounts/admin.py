from django.contrib import admin

from .models import UserLibrary, User

admin.site.register(User)
admin.site.register(UserLibrary)