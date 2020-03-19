from django.db import models

# Create your models here.
class Sexe(models.Model):

    nom           = models.CharField(max_length=100)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

class Localite(models.Model):

    nom           = models.CharField(max_length=100)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

class Dren(models.Model):

    nom           = models.CharField(max_length=100)
    email         = models.EmailField(blank=True)
    contact       = models.CharField(max_length=8)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

  
class Type_Ecole(models.Model):#exemple : COLLEGE/LYCEE

    nom           = models.CharField(max_length=100)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

class Type_Statut_Ecole(models.Model):#exemple : PRIVE/PUBLIC

    nom           = models.CharField(max_length=100)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

class Type_Enseignement(models.Model):#exemple : GENERAL/TECHNIQUE

    nom           = models.CharField(max_length=100)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nom

class Type_Matiere(models.Model):

    nom           = models.CharField(max_length=100) 
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nom



class Matiere(models.Model):

    nom           = models.CharField(max_length=100)
    coefficient   = models.IntegerField() 
    type_matiere  = models.ForeignKey(Type_Matiere, on_delete=models.CASCADE)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nom

class Proviseur(models.Model):

    nom               = models.CharField(max_length=100)
    prenom            = models.CharField(max_length=100)
    matricule         = models.CharField(max_length=9)
    contact           = models.CharField(max_length=8)
    sexe              = models.ForeignKey(Sexe, on_delete=models.CASCADE)
    email             = models.EmailField(blank=True) 
    date_de_naissance = models.DateField()
    status            = models.BooleanField(default=True)
    date_creation     = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nom 

class Etablissement(models.Model):

    nom               = models.CharField(max_length=100)
    dren              = models.ForeignKey(Dren, on_delete=models.CASCADE)
    type_ecole        = models.ForeignKey(Type_Ecole, on_delete=models.CASCADE)
    type_statut       = models.ForeignKey(Type_Statut_Ecole, on_delete=models.CASCADE)
    type_enseignement = models.ForeignKey(Type_Enseignement, on_delete=models.CASCADE)
    localite          = models.ForeignKey(Localite, on_delete=models.CASCADE)
    proviseur         = models.ForeignKey(Proviseur, on_delete=models.CASCADE)
    email             = models.EmailField(blank=True)
    contact           = models.CharField(max_length=8)
    status            = models.BooleanField(default=True)
    date_creation     = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom

 



class Educateur(models.Model):

        nom               = models.CharField(max_length=100)
        prenom            = models.CharField(max_length=100)
        matricule         = models.CharField(max_length=9)
        etablissement     = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
        sexe              = models.ForeignKey(Sexe, on_delete=models.CASCADE)
        email             = models.EmailField(blank=True)
        contact           = models.CharField(max_length=8)
        date_de_naissance = models.DateField()
        status            = models.BooleanField(default=True)
        date_creation     = models.DateField(auto_now=True)


        def __str__(self):
           return self.nom 


class Professeur(models.Model):

    nom               = models.CharField(max_length=100)
    prenom            = models.CharField(max_length=100)
    matricule         = models.CharField(max_length=9)
    matiere           = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    sexe              = models.ForeignKey(Sexe, on_delete=models.CASCADE)
    email             = models.EmailField(blank=True)
    contact           = models.CharField(max_length=8) 
    date_de_naissance = models.DateField()
    status            = models.BooleanField(default=True)
    date_creation     = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom 

class Niveau(models.Model):

    nom           = models.CharField(max_length=100) 
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.nom 

class Classe(models.Model):

    nom                  = models.CharField(max_length=100) 
    tablissement         =  models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    niveau               =  models.ForeignKey(Niveau, on_delete=models.CASCADE)
    professeur_principal = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    status               = models.BooleanField(default=True)
    date_creation        = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nom 

class Eleve(models.Model):

    nom               = models.CharField(max_length=100)
    prenom            = models.CharField(max_length=100)
    matricule         = models.CharField(max_length=9)
    contact           = models.CharField(max_length=8)
    etablissement     = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    classe            = models.ForeignKey(Classe, on_delete=models.CASCADE)
    chef            = models.BooleanField(default=False)
    sexe              = models.ForeignKey(Sexe, on_delete=models.CASCADE)
    email             = models.EmailField(blank=True) 
    date_de_naissance = models.DateField()
    status            = models.BooleanField(default=True)
    date_creation     = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom     



class Professeur_Etablissement(models.Model):
    
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    status            = models.BooleanField(default=True)
    date_creation     = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.professeur.nom
    




class Etablissement_Niveau_Educateur(models.Model):

    etablissement =  models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    niveau        =  models.ForeignKey(Niveau, on_delete=models.CASCADE)
    educateur     =  models.ForeignKey(Educateur, on_delete=models.CASCADE)
    status        = models.BooleanField(default=True)
    date_creation = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.etablissement.nom 



class Repartition(models.Model):

    etablissement        =  models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    classe               =  models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere              =  models.ForeignKey(Matiere , on_delete=models.CASCADE)
    professeur           = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    status               = models.BooleanField(default=True)
    date_creation        = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.etablissement.nom

