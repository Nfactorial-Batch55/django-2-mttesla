from django.contrib import admin
from .models import Comment, News
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')

    def has_comments(self, obj):
        return Comment.objects.filter(news=obj).exist()
    has_comments.boolean = True
    has_comments.short_description = 'Has comments'



