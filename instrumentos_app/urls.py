from django.urls import path
from instrumentos_app import views
urlpatterns = [
    path("instrumentos", views.inicio_vistaInstrumento, name="instrumentos"),
    path("registrarInstrumento/", views.registrarInstrumento, name="registrarInstrumento" ),
    path("seleccionarInstrumentos/<codigo>", views.seleccionarInstrumentos, name="seleccionarInstrumentos"),
    path("editarInstrumento/", views.editarInstrumento, name="editarInstrumento"),
    path("borrarInstrumento/<codigo>", views.borrarInstrumento, name="borrarInstrumento")
    
]
