# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from article.models import Article, Comments
from django.contrib import admin

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date']
    inlines = [ArticleInline]
    list_filter = ['article_date']


admin.site.register(Article,ArticleAdmin)

