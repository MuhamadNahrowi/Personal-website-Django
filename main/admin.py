from django.contrib import admin
from .models import Blog, Kategori, Book

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields:[
        'slug',
        'update',
        'publish',
    ]


admin.site.register(Blog)
admin.site.register(Kategori)
admin.site.register(Book)