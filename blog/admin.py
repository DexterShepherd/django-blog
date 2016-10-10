from django.contrib import admin
from blog.models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepolulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(Category)
