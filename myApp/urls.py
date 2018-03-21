from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('page_telechargement/', views.ajouter_document),
	path('validation_telechargement/', views.validation_telechargement),
	path('ajouter_fichier_seul/', views.ajouter_fichier_seul),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





