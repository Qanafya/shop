from django.contrib import admin

# Register your models here.
from .models import *

class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

admin.site.register(Users)
admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Details)
admin.site.register(Comments)
admin.site.register(Admins, PostsAdmin)

