from django.contrib import admin
from news.models import News

class Newsadmin(admin.ModelAdmin):
    list_display=('news_title', 'news_desc')
    
admin.site.register(News, Newsadmin)

# Register your models here.

