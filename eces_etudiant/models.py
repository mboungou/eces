from django.db import models

# Create your models here.
class Etudiant(models.Model):
	matricule=models.CharField(max_length=100)
	nom=models.CharField(max_length=100)
	prenom=models.CharField(max_length=100)
	adress=models.CharField(max_length=100)
	option=models.CharField(max_length=100)
	niveau=models.CharField(max_length=100)
	description=models.TextField()
	photo=models.ImageField()

	def __str__ (self):
		return self.nom.title()
