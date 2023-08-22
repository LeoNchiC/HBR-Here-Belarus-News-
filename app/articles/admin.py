from django.contrib import admin

from .models import Article, Comment, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title',)
    inlines = (ImageInline, )

admin.site.register(Comment)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('article', )
