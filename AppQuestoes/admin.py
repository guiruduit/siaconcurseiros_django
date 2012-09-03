# -*- encoding: utf-8 -*-

# Django
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin

# AppQuestoes
from models import Banca, Concurso, Prova, Disciplina, Assunto, Questao, QuestaoDeMultiplaEscolha, QuestaoDeVerdadeiroOuFalso, UserProfile, AreaDeAtuacao

admin.site.unregister(User)
admin.site.unregister(Group)

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]
#    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

class QuestaoAdmin(admin.ModelAdmin):

    class Media:
#        js = ['http://localhost:8000/media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/media/tinymce_setup/tinymce_setup.js', ]
        js = ['/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/tinymce_setup/tinymce_setup.js', ]

admin.site.register(User, UserProfileAdmin)
admin.site.register(Banca)
admin.site.register(Concurso)
admin.site.register(Prova)
admin.site.register(Disciplina)
admin.site.register(Assunto)
# admin.site.register(Questao)
#admin.site.register(QuestaoDeMultiplaEscolha, QuestaoDeMultiplaEscolhaAdmin)
admin.site.register(QuestaoDeMultiplaEscolha, QuestaoAdmin)
admin.site.register(QuestaoDeVerdadeiroOuFalso, QuestaoAdmin)
#admin.site.register(UserProfile)
admin.site.register(AreaDeAtuacao)
