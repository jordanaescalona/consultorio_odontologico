from django.db import models
from datetime import datetime

from django.db.models.fields import related
# Create your models here.
class Localidad(models.Model):
    nombre = models.CharField(max_length=150)
    cp = models.IntegerField('Código Postal')

    def __str__(self):
        return self.nombre
    
class Persona(models.Model):
    num_doc = models.CharField('N° de documento',max_length=20,primary_key=True,unique=True)
    nombre = models.CharField('Nombre/s',max_length=150)
    apellido = models.CharField('Apellido/s',max_length=150)
    num_cuit = models.CharField('N° de CUIT/CUIL',max_length=20,null=True,blank=True)
    fecha_nac = models.DateField("Fecha de nacimiento",default=datetime.now)
    telefono = models.CharField("N° de teléfono ",max_length=50,null=True,blank=True)
    email = models.EmailField("E-mail",null=True,blank=True)
    direccion = models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
    class Meta:
        abstract = True



class ObraSocial(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250,blank=True,null=True)
    disponible = models.BooleanField(default=True)
    telefono = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

class Paciente(Persona):    
    hc = models.IntegerField('N° historia clínica',null=True,blank=True)
    obra_social = models.ForeignKey(ObraSocial,verbose_name='Obra Social',on_delete=models.PROTECT,related_name='paciente_obraSocial',default='Ninguna')
    titular_familiar = models.CharField("Familiar titular",max_length=250,null=True,blank=True,default="No requiere")

        


class Calendario(models.Model):
    DIA_CHOICES = (
        ('L','Lunes'),
        ('M','Martes'),
        ('Mi','Miercoles'),
        ('J','Jueves'),
        ('V','viernes')
    )
    dia = models.CharField('Día de la semana',max_length=9,choices=DIA_CHOICES,default='L')
    hora = models.DateTimeField()

    def __str__(self):
        return self.dia

class Profesional(Persona):
    
    matricula = models.IntegerField(unique=True)
    especialidad = models.CharField(max_length=150)
    


class Calendario_turnos(models.Model):
    profesional = models.ForeignKey(Profesional,on_delete=models.CASCADE,related_name='profesional_calendario_turnos')
    dia_hora = models.ForeignKey(Calendario,on_delete=models.CASCADE,related_name='dia_hora_calendario_turnos')

    def __str__(self):
        return self.profesional


class Establecimiento(models.Model):
    nombre = models.CharField(max_length=150)
    razon_social = models.CharField(max_length=250)
    direccion = models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    cp = models.IntegerField('Código Postal')
    
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=250)
    web = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,related_name='paciente_turno')
    medico = models.ForeignKey(Profesional,on_delete=models.CASCADE,related_name='medico_turno')
    fecha = models.DateTimeField()
    

    ESTADO = (
        ('Reservado','Reservado'),
        ('Confirmado','Confirmado'),
        ('Cancelado','Cancelado')
    )
    estado = models.CharField(max_length=10,choices=ESTADO,default='Reservado')

    def __str__(self):
        return self.fecha

    class Meta:
        ordering = ['fecha']


class PiezaDental(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Prestacion(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    pieza_dental = models.ManyToManyField(PiezaDental,related_name='pieza_dental_prestacion')

    def __str__(self):
        return self.nombre
class Tratamiento(models.Model):
    profesional = models.ManyToManyField(Profesional,related_name='medico_tratamiento')
    prestacion = models.ManyToManyField(Prestacion,related_name='prestacion_tratamiento')
    fecha = models.DateField(default=datetime.now)
    observacion = models.TextField()

    def __str__(self):
        return self.profesional

class FichaMedica(models.Model):
    establecimiento = models.ManyToManyField(Establecimiento,related_name='establecimiento_ficha_medica')
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE,related_name='paciente_ficha_medica')
    fecha_alta = models.DateField(auto_now_add=True)

    
    FACTORES = (
        ('a_mas','A+'),
        ('a_menos','A-'),
        ('b_mas','B+'),
        ('b_menos','B-'),
        ('ab_mas','AB+'),
        ('ab_menos','AB-'),
        ('o_mas','O+'),
        ('o_menos','O-')
    )
    
    factor = models.CharField("Factor sanguineo",max_length=15,choices=FACTORES)
    antecedentes = models.TextField("Antecedentes médicos")
    medicacion = models.TextField()
    prestacion = models.ManyToManyField(Prestacion,related_name='prestacion_ficha_medica')
    historia_clinica = models.ManyToManyField(Tratamiento,related_name='historia_clinica_ficha')

    def __str__(self):
        return self.paciente    
