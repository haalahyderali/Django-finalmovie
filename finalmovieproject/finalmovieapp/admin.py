from django.contrib import admin
from . models import Movie
from . models import Category,Movie,Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','date','actors','category','user']
    list_editable = ['date','actors','user']
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Movie, MovieAdmin)

admin.site.register(Comment)
