from django.contrib import admin
from content.models import Curso

# Register your models here.


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'link', 'data_criacao')
    list_filter = ('usuario', 'nome',)

admin.site.register(Curso, CursoAdmin)