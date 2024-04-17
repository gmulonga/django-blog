from django.contrib import admin

# Register your models here.
from .models import Post

# connects the post model with the post model admin
class PostAdmin(admin.ModelAdmin):
    # displaying these items in the model, {title can be replaced with __str__ / __unicode__}
    list_display = ["title", "timestamp"]
    class Meta:
        model = Post

# used to register the Post in the admin
admin.site.register(Post, PostAdmin)