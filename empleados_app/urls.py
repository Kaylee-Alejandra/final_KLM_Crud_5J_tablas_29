from django.urls import path
from empleados_app import views
urlpatterns = [
    path("empleados", views.inicio_vistaEmpleado, name="empleados"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado" ),
    path("seleccionarEmpleado/<id_empleado>", views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/", views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<id_empleado>", views.borrarEmpleado, name="borrarEmpleado")
    
]
