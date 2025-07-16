from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "add_date", "cover"]
    list_display_links = ["title", "add_date"]
    list_filter = ["add_date", "price"]
    search_fields = ["title", "description"]