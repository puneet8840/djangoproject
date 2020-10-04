from django.contrib import admin
from blog.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','slug','created','publish','updates','body','status']
    list_filter=['title','author','created']
    prepopulated_fields={'slug':('title',)}
    search_fields=['title','body']
    raw_id_fields='author',
    date_hierarchy='publish'
    ordering=['publish','author']
class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','created','updated','active','email','body']
    list_filter=('name','email')
    search_fields=('name','email')
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
