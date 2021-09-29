from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def agregar_persona(request):
    if request.method == 'POST':
        persona = PersonaForm(request.POST)

        if persona.is_valid():
            persona.save()
            return redirect('Odonto:index')
    else:
        persona = PersonaForm()
        return render(request,'persona/agregar_persona.html',{
            'persona':persona
        })

def listado_personas(request):
    personas = Persona.objects.all()
    return render(request,'persona/listado_personas.html',{
        'personas':personas
    })

def editar_persona(request,id):
    persona = get_object_or_404(Persona,num_doc=id)
    if request.method == 'POST':
        form = PersonaForm(data=request.POST,instance=persona)
        if form.is_valid():
            form.save()
    else:
        form = PersonaForm(instance=persona)
        return render(request,'persona/editar_persona.html',{
            'persona':persona,
            'form':form
        })

    return redirect('Odonto:listado_personas')

def eliminar_persona(request,id):
    persona = get_object_or_404(Persona,num_doc=id)
    persona.delete()
    return redirect('Odonto:listado_personas')

def listado_pacientes(request):
    pacientes = Paciente.objects.all()

    return render(request,'paciente/listado_pacientes.html',{
        'pacientes':pacientes
    })

def agregar_paciente(request):
    if request.method == 'POST':
        paciente = PacienteForm(request.POST)
                   
        if paciente.is_valid():
               
            paciente.save()
            return redirect('Odonto:index')
    else:
        paciente = PacienteForm()

        return render(request,'paciente/agregar_paciente.html',{

            'paciente':paciente
        })

def editar_paciente(request,id):
    paciente = get_object_or_404(Paciente,id=id)
    if request.method == 'POST':
        form = PacienteForm(data=request.POST,instance=paciente)
        if form.is_valid():
            form.save()
    else:
        form = PacienteForm(instance=paciente)
        return render(request,'paciente/editar_paciente.html',{
            'form':form
        })
    return redirect('Odonto:listado_pacientes')

def eliminar_paciente(request,id):
    paciente = get_object_or_404(Paciente,id=id)
    paciente.delete()
    return redirect('Odonto:listado_pacientes')

def agregar_profesional(request):
    if request.method == 'POST':
        profesional = ProfesionalForm(request.POST)

        if profesional.is_valid():
            profesional.save()
            return redirect('Odonto:index')
    else:
        profesional = ProfesionalForm()
        return render(request,'profesional/agregar_profesional.html',{
            'profesional':profesional
        })

def listado_profesionales(request):
    profesionales = Profesional.objects.all()
    return render(request,'profesional/listado_profesionales.html',{
        'profesionales':profesionales
    })

def editar_profesional(request,id):
    profesional = get_object_or_404(Profesional,matricula=id)
    if request.method == 'POST':
        form = ProfesionalForm(data=request.POST,instance=profesional)
        if form.is_valid():
            form.save()
    else:
        form = ProfesionalForm(instance=profesional)
        return render(request,'profesional/editar_profesional.html',{
            'form':form
        })
    return redirect('Odonto:listado_profesionales')

def eliminar_profesional(request,id):
    profesional = get_object_or_404(Profesional,matricula=id)
    profesional.delete()
    return redirect('Odonto:listado_profesionales')

def agregar_os(request):
    if request.method == 'POST':
        obrasocial = ObraSocialForm(request.POST)

        if obrasocial.is_valid():
            obrasocial.save()
            return redirect('Odonto:index')
    else:
        obrasocial = ObraSocialForm()
        return render(request,'obrasocial/agregar_os.html',{
            'os':obrasocial
        }) 

def listado_os(request):
    obrasociales = ObraSocial.objects.all()
    return render(request,'obrasocial/listado_os.html',{
        'obs':obrasociales
    })   

def editar_os(request,id):
    os = get_object_or_404(ObraSocial,id=id)
    if request.method == 'POST':
        form = ObraSocialForm(data=request.POST,instance=os)
        if form.is_valid():
            form.save()
    else:
        form = ObraSocialForm(instance=os)
        return render(request,'obrasocial/editar_os.html',{
            'form':form
        })

def eliminar_os(request,id):
    os = get_object_or_404(ObraSocial,id=id)
    paciente_os = Paciente.objects.filter(obra_social=os)
    
    if paciente_os:
        messages.error(request,'No se puede eliminar la Obra Social porque se encuentra a sociada a un usuario')
    else:
        os.delete()
    
    return redirect('Odonto:listado_os')

def establecimiento(request):
    establecimientos = Establecimiento.objects.all()

    if establecimientos:
        establecimiento = Establecimiento.objects.latest('id')

        if request.method == 'POST':
            form = EstablecimientoForm(data=request.POST,instance=establecimiento)
            if form.is_valid():
                form.save()
        else:
            form = EstablecimientoForm(instance=establecimiento)
            return render(request,'establecimiento/establecimiento.html',{
                'form':form,
                'establecimientos':establecimientos
            })
        return redirect('Odonto:index')
    else:
        return render(request,'establecimiento/establecimiento.html',{
            'establecimientos':establecimientos
        })


def agregar_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Odonto:index')
    else:
        form = EstablecimientoForm()
        return render(request,'establecimiento/agregar_establecimiento.html',{
            'form':form
        })

def ver_turnos(request):
    turnos = Turno.objects.all()
    
    diccionario ={}
    for turno in turnos:
        diccionario['title'] = turno.paciente.persona
        diccionario['start'] = turno.fecha

    print(diccionario)
        
    return render(request,'turno/turno.html',{
        'turnos':turnos,
        'diccionario':diccionario
    }) 

def agregar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Odonto:index')
    else:
        form = TurnoForm()
        return render(request,'turno/nuevo_turno.html',{
            'form':form
        })

def modificar_turno(request,id):
    turno = get_object_or_404(Turno,id=id)
    if request.method == 'POST':
        form = TurnoForm(data=request.POST,instance=turno)
        if form.is_valid():
            form.save()
    else:
        form = TurnoForm(instance=turno)
        return render(request,'turno/modificar_turno.html',{
            'form':form
        })
    return redirect('Odonto:turnos')