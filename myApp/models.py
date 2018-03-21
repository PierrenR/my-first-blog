from django.db import models


def renommage(instance, nom_fichier):
	return "{}-{}".format(instance.id, nom_fichier)


class Document(models.Model):
	nom = models.CharField(max_length=255)
	file = models.FileField()
	description = models.TextField(null=True)
	def __unicode__(self):
		return "%s" % self.titre
  
class Document_seul(models.Model):
	file = models.FileField()
	def __unicode__(self):
		return "%s" % self.titre
	  
class nombre_fichiers (models.Model):
	comptage = models.IntegerField()
	#def __unicode__(self):
		#return "%s" % self.titre