from django.contrib import admin
from . models import Etudiant
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group


class EtudiantAdmin(admin.ModelAdmin):
	list_display=['matricule','nom','prenom','adress','option','niveau','description','photo']
	list_display_links=['matricule','nom','prenom','adress','option','niveau','description','photo']
	search_fields=['matricule','nom','prenom','adress','option','niveau','description','photo']

admin.site.register(Etudiant,EtudiantAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)

class Eces(AdminSite):
	site_header="ECES ETUDIANT"

#admin.site = Eces(name='admin')
# Register your models here.
