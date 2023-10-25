from django.shortcuts import render

from MiApp2.models import Trabajo, Empleado

from .forms import CrearTrabajoForm, CrearEmpleadoForm, CrearClientesForm, UserRegisterForm

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView

# Create your views here.

def mostrar_trabajo(request):

    t1 = Trabajo(nombre='Programador', sueldo='$150000')
    t2 = Trabajo(nombre='Tecnico', sueldo='$50000')

    return render(request, 'MiApp2/trabajo.html', {'trabajo':[t1, t2]})

def mostrar_empleado(request):

    empleados = Empleado.objects.all()

    context = {'empleados': empleados}

    return render(request, 'MiApp2/mostrar_empleados.html', context=context)


def mostrar_index(request):


        return render(request, 'MiApp2/home.html')


def crear_trabajo(request):
    if request.method == 'POST':
            
                formulario = CrearTrabajoForm(request.POST)

                if formulario.is_valid():
            
                    formulario_limpio = formulario.cleaned_data

                    trabajo = Trabajo(nombre=formulario_limpio['nombre'], sueldo=formulario_limpio['sueldo'])

                    trabajo.save()

                    return render(request, 'MiApp2/home.html')
        
        
    else:
        formulario = CrearTrabajoForm()

    return render(request, 'MiApp2/crear_trabajo.html', {'formulario': CrearTrabajoForm})

def crear_empleado(request):

    if request.method == 'POST':
        
        formulario = CrearEmpleadoForm(request.POST)

        if formulario.is_valid():
        
            formulario_limpio = formulario.cleaned_data

            empleado = Empleado(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], 
                                email=formulario_limpio['email'], profesion=formulario_limpio['profesion']) 

            empleado.save()

            return render(request, 'MiApp2/home.html')
    else:
        formulario = CrearEmpleadoForm()

        return render(request, 'MiApp2/crear_empleado.html', {'formulario': CrearEmpleadoForm})
        

def buscar_trabajo(request):

    if request.GET.get('sueldo', False):
        sueldo = request.GET['sueldo']
        trabajos = Trabajo.objects.filter(sueldo__icontains=sueldo)

        return render(request, 'MiApp2/buscar_sueldo.html', {'trabajos': trabajos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp2/buscar_sueldo.html', {'respuesta': respuesta})


def buscar_empleado(request):

    if request.GET.get('email', False):
        email = request.GET['email']
        empleados = Empleado.objects.filter(email__icontains=email)

        return render(request, 'MiApp2/buscar_empleado.html', {'empleados': empleados})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp2/buscar_empleado.html', {'respuesta': respuesta})


def soporte(request):
    
    if request.GET.get('consulta', False):
        consulta = request.GET['consulta']
        Soporte = Soporte.objects.filter(consulta__icontains=consulta)

        return render(request, 'MiApp2/soporte.html', {'soporte': soporte})
    else:
        respuesta = 'No hay datos'
    return render(request, 'MiApp2/soporte.html', {'respuesta': respuesta})

def eliminar_empleado(request, empleado_id):

    empleado = Empleado.objects.get(id=empleado_id)

    empleado.delete()


    empleados = Empleado.objects.all()

    context = {'empleados': empleados}

    return render(request, 'MiApp2/mostrar_empleados.html', context=context)

def actualizar_empleado(request, empleado_id):
    
    empleado = Empleado.objects.get(id=empleado_id)

    if request.method == 'POST':
    
        formulario = CrearEmpleadoForm(request.POST)

        if formulario.is_valid():
        
            formulario_limpio = formulario.cleaned_data

            empleado.nombre = formulario_limpio ['nombre']
            empleado.apellido = formulario_limpio ['apellido']
            empleado.email = formulario_limpio ['email']
            empleado.profesion = formulario_limpio ['profesion']



            empleado.save()

            return render(request, 'MiApp2/home.html')
    else:
        formulario = CrearEmpleadoForm(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido,
                                                'email': empleado.email, 'profesion': empleado.profesion})
        
    return render(request, 'MiApp2/actualizar_empleado.html', {'formulario': CrearEmpleadoForm, 'empleado': empleado})

def actualizar_trabajo(request, trabajo_id):
    
    trabajo = Trabajo.objects.get(id=trabajo_id)

    if request.method == 'POST':
    
        formulario = CrearTrabajoForm(request.POST)

        if formulario.is_valid():
        
            formulario_limpio = formulario.cleaned_data

            trabajo.nombre = formulario_limpio ['nombre']
            trabajo.sueldo = formulario_limpio ['sueldo']



            trabajo.save()

            return render(request, 'MiApp2/home.html')
    else:
        formulario = CrearTrabajoForm(initial={'nombre': trabajo.nombre, 'sueldo': trabajo.sueldo})
        
    return render(request, 'MiApp2/actualizar_trabajo.html', {'formulario': CrearTrabajoForm, 'trabajo': trabajo})


def eliminar_trabajo(request, trabajo_id):

    trabajo = Trabajo.objects.get(id=trabajo_id)

    trabajo.delete()


    trabajos = Trabajo.objects.all()

    context = {'trabajos': trabajos}

    return render(request, 'MiApp2/mostrar_trabajos.html', context=context)

class TrabajoList(ListView):

    model = Trabajo
    template_name = 'MiApp2/trabajos_list.html'

class TrabajoDetailView(DetailView):
    
    model = Trabajo
    template_name = 'MiApp2/trabajo_detalle.html'

class TrabajoCreateView(CreateView):

    model = Trabajo
    success_url = '/trabajo_list'
    fields = ['nombre', 'sueldo']

class TrabajoUpdateView(UpdateView):

    model = Trabajo
    success_url = '/trabajo_list'
    fields = ['nombre', 'sueldo']

class TrabajoDeleteView(DeleteView):

    model = Trabajo
    success_url = '/trabajo_list'

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request,'MiApp2/home.html', {"mensaje":f"¡Bienvenido {usuario}!"} )
            else:
                    return render(request,'MiApp2/home.html', {"mensaje":"¡Error, datos incorrectos!"} )
            
        else: 
                return render(request,'MiApp2/home.html', {"mensaje":"¡Error, formulario erroneo!"} )
        
    form = AuthenticationForm()

    return render(request,'MiApp2/login.html', {'form':form})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'MiApp2/home.html', {"mensaje":"¡Usuario Registrado!"})
        
    else:
            form = UserRegisterForm()
    
    return render(request,'MiApp2/register.html', {'form':form})

