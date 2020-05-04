from django.contrib import admin
from .models import Post
# Register your models here.

#torna o modelo visível na página de admin
admin.site.register(Post)