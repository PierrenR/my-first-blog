from .models import Document,Document_seul
from django import forms
import datetime
from django.forms import ModelForm

class DocumentForm(forms.Form):
    nom = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    file = forms.FileField()
	
	
class Form_dossier_seul(forms.Form):
    file = forms.FileField()	
	
	