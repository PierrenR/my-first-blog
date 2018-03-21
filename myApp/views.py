from django.shortcuts import render
from .models import Document,Document_seul
from .models import Document_seul
from .models import nombre_fichiers
from .forms import DocumentForm,Form_dossier_seul


def ajouter_document(request):
	if request.method == 'POST': 
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid(): 
			nom = form.cleaned_data['nom']
			file = form.cleaned_data['file']
			description = form.cleaned_data['description']
			envoi = 1
			try:
				doc = Document.objects.get(nom = nom)
			except Document.DoesNotExist:
				doc = Document(nom = nom, file = file, description = description)
				doc.save()
				message = "Le document {a} a bien été ajouté !".format(a = nom)  
				return render(request, 'myApp/ok.html')
				#return render(request, 'myApp/validation_telechargement/')
		else:
			message = "Le document {a} existe déjà !".format(a = nom)
	return render(request, 'myApp/ajouter_doc.html', locals())

   
def ajouter_fichier_seul(request):
	
	form = Form_dossier_seul(request.POST or None, request.FILES)	# pour ajouter champ obligatoire :		, request.FILES
	
	if form.is_valid():
		file = form.cleaned_data["file"]
		doc = Document_seul(file = file)
		
		from os.path import basename
		a = file.name							  # les differents attributs de FieldFile : https://docs.djangoproject.com/fr/2.0/ref/models/fields/
		b = file.size
		#c = file.open
		liste_fichiers = os.listdir("./media")
		if a in liste_fichiers : 
			message_error_1 = "un fichier de même nom existe déjà"
		elif len(a) != 11  :
			message_error_1 = "mauvais format fichier"
		else :
			doc.save()
			return render(request, 'myApp/ok.html', locals())
		
		
	return render(request, 'myApp/document_seul.html', locals() )
   

   
   
   
   
import os
def validation_telechargement(request):

	#a = nombre_fichiers()
	#avant = a.comptage

	list_fichiers = os.listdir("./media") 	
	
	c = int(len(list_fichiers))
	t = nombre_fichiers(comptage=c)
	tt = t.comptage
	# t.save()
	
	#t = nombre_fichiers.comptage
	
	if "Affaires.xlsx" in list_fichiers :
		d = "est present"
		os.remove("./media/Affaires.xlsx")
	
	
	return render(request, 'myApp/ok2.html', locals())
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def voir_contacts(request):   



	return render(
		request, 
		'myApp/ok.html', 
		{'documents': Document.objects.all()}
	)
	
	
	
	
	
	
	