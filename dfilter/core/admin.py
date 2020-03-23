from django.contrib import admin

# Register your models here.
from .models import Author,Category,Journal
@admin.register(Author)
class Author(admin.ModelAdmin):
    pass
@admin.register(Category)
class Category(admin.ModelAdmin):
    pass
@admin.register(Journal)
class Journal(admin.ModelAdmin):
    pass