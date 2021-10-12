from django.urls import path
from .views import *


app_name = "Odonto"
urlpatterns = [
     path('',index,name='index'),
     path('pacientes/listado_pacientes',listado_pacientes,name="listado_pacientes"),
     path('pacientes/agregar_paciente',agregar_paciente,name="agregar_paciente"),
     path('pacientes/editar/<int:id>',editar_paciente,name='editar_paciente'),
     path('pacientes/eliminar/<int:id>',eliminar_paciente,name='eliminar_paciente'),
     path('persona/agregar_persona',agregar_persona,name="agregar_persona"),
     path('persona/lista_personas',listado_personas,name="listado_personas"),
     path('persona/editar_persona/<int:id>',editar_persona,name="editar_persona"),
     path('persona/eliminar/<int:id>',eliminar_persona,name='eliminar_persona'),
     path('profesional/agregar_profesional',agregar_profesional,name='agregar_profesional'),
     path('profesional/listar_profesionales',listado_profesionales,name='listado_profesionales'),
     path('profesional/editar/<int:id>',editar_profesional,name='editar_profesional'),
     path('profesional/eliminar/<int:id>',eliminar_profesional,name='eliminar_profesional'),
     path('obrasocial/agregar',agregar_os,name='agregar_os'),
     path('obrasocial/listado',listado_os,name='listado_os'),
     path('obrasocial/editar/<int:id>',editar_os,name='editar_os'),
     path('obrasocial/eliminar/<int:id>',eliminar_os,name='eliminar_os'),
     path('establecimiento',establecimiento,name='establecimiento'),
     path('establecimiento/agregar',agregar_establecimiento,name='agregar_establecimiento'),
     path('turnos',ver_turnos,name='turnos'),
     path('turno/nuevo',agregar_turno,name='agregar_turno'),
     path('turno/editar/<int:id>',modificar_turno,name='editar_turno'),
     path('turno/eliminar/<int:id>',eliminar_turno,name="eliminar_turno"),
     path('login',login_view,name='login'),
     path('logout',logout_view,name='logout'),
]