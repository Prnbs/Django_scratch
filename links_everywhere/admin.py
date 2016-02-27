from django.contrib import admin
from .models import Tags, URL, User
# Register your models here.

admin.site.register(Tags)
admin.site.register(URL)
admin.site.register(User)