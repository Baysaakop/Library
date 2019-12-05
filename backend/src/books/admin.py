from django.contrib import admin

from .models import Category, Language, Book

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Book)
