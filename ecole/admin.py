

from django.contrib import admin
from .models import (Sexe,
                     Localite,
                     Dren,
                     Type_Ecole,
                     Type_Statut_Ecole,
                     Type_Enseignement,
                     Type_Matiere,
                     Matiere,
                     Proviseur,
                     Etablissement,
                     Educateur,
                     Professeur,
                     Niveau,
                     Classe,
                     Eleve,
                     Professeur_Etablissement,
                     Etablissement_Niveau_Educateur,
                     Repartition
                     )


class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom','tablissement','niveau','professeur_principal','status')

class DrenAdmin(admin.ModelAdmin):
    list_display = ('nom','email','contact','status')


class EducateurAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','matricule','etablissement','sexe','email','contact','date_de_naissance','status')

class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','matricule','contact','etablissement','classe','chef','sexe','email','date_de_naissance','status')

class Etablissement_educateur_Admin(admin.ModelAdmin):
    list_display = ('etablissement','niveau','educateur','status')


class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom','dren','type_ecole','type_statut','type_enseignement','localite','proviseur','email','contact','status')

class LocaliteAdmin(admin.ModelAdmin):
    list_display = ('nom','status')


class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom','coefficient','type_matiere','status')


class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom','status')


class Professeur_etablissement_Admin(admin.ModelAdmin):
    list_display = ('professeur','etablissement','status')


class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','matricule','matiere','sexe','email','contact','date_de_naissance','status')

class ProviseurAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','matricule','contact','sexe','email','date_de_naissance','status')


class RepartitionAdmin(admin.ModelAdmin):
    list_display = ('etablissement','classe','matiere','professeur','status')

class SexeAdmin(admin.ModelAdmin):
    list_display = ('nom','status')

class Type_Ecole_Admin(admin.ModelAdmin):
    list_display = ('nom','status')


class Type_Enseignement_Admin(admin.ModelAdmin):
    list_display = ('nom','status')

class Type_Matiere_Admin(admin.ModelAdmin):
    list_display = ('nom','status')

class Type_Statut_Ecole_Admin(admin.ModelAdmin):
    list_display = ('nom','status')




# Register your models here.
admin.site.register(Sexe                    ,                           SexeAdmin)
admin.site.register(Dren                    ,                           DrenAdmin)
admin.site.register(Eleve                   ,                          EleveAdmin)
admin.site.register(Niveau                  ,                         NiveauAdmin)
admin.site.register(Classe                  ,                         ClasseAdmin)
admin.site.register(Matiere                 ,                        MatiereAdmin)
admin.site.register(Localite                ,                       LocaliteAdmin)
admin.site.register(Proviseur               ,                      ProviseurAdmin)
admin.site.register(Educateur               ,                      EducateurAdmin)
admin.site.register(Professeur              ,                     ProfesseurAdmin)
admin.site.register(Type_Ecole              ,                    Type_Ecole_Admin)
admin.site.register(Repartition             ,                    RepartitionAdmin)
admin.site.register(Etablissement           ,                  EtablissementAdmin)
admin.site.register(Type_Matiere            ,                  Type_Matiere_Admin)
admin.site.register(Type_Statut_Ecole       ,             Type_Statut_Ecole_Admin)
admin.site.register(Type_Enseignement       ,             Type_Enseignement_Admin)
admin.site.register(Etablissement_Niveau_Educateur, Etablissement_educateur_Admin)
admin.site.register(Professeur_Etablissement,      Professeur_etablissement_Admin)

