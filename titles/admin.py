
from django.contrib import admin

from .models import Title, Category, Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'rating', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('year', 'rating')
    empty_value_display = '-none-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = '-none-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = '-none-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
