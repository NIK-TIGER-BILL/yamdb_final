from django.contrib import admin

from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-none-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'review_id', 'text', 'author', 'pub_date')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-none-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
