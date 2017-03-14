# Register your models here.

from django.contrib import admin
from .models import Post  #importuje model Post z models.py

admin.site.register(Post) #by model był widoczny w panelu admina musimy go zarejestrować



