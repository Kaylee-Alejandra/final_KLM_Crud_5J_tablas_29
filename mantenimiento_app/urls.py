from django.urls import path
from mantenimiento_app import views
urlpatterns = [
    path("mantenimiento", views.inicio_vistaMantenimiento, name="mantenimiento"),
    path("registrarMantenimiento/", views.registrarMantenimiento, name="registrarMantenimiento" ),
    path("seleccionarMantenimiento/<id_mantenimiento>", views.seleccionarMantenimiento, name="seleccionarMantenimiento"),
    path("editarMantenimiento/", views.editarMantenimiento, name="editarMantenimiento"),
    path("borrarMantenimiento/<id_mantenimiento>", views.borrarMantenimiento, name="borrarMantenimiento")
]