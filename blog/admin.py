from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post) #Habilita al admin para registrar con nuestro modelo
admin.site.register(Comment)
