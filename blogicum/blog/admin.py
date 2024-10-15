# ice_cream/admin.py
from django.contrib import admin

# Register your models here.

# Из модуля models импортируем модель Category...
from .models import Category
from .models import Location
from .models import Post

# ...и регистрируем её в админке:
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
