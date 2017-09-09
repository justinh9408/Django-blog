from django.contrib import admin
from bloger.models import *

# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):



admin.site.register(Article)
admin.site.register(Tag)