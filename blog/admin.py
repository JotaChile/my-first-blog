from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post) #Habilita al admin para registrar con nuestro modelo
