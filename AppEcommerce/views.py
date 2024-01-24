from django.shortcuts import render,get_object_or_404,redirect
from AppEcommerce.models import Productos,ProductosCategorias,ProductosMarcas,UserProfile,Newsletter
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Q

from django.utils.translation import activate

from .forms import UserProfileForm, ProductosForm, ContactoForm
from django.core.mail import send_mail



def index(request):

    productos = Productos.objects.all()[:12]
    return render(request, "AppEcommerce/index.html", {'productos': productos})  

def nosotros(request):

    return render(request, "AppEcommerce/nosotros.html", {})  

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Configura tu correo electrónico y envía el mensaje
            destinatario = 'tomasdegaetano.dark@gmail.com'
            asunto = f'Nuevo mensaje de contacto de {nombre}'
            cuerpo_mensaje = f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'


            send_mail(asunto, cuerpo_mensaje, email, [destinatario] )

            return render(request, 'AppEcommerce/agradecimiento.html')
    else:
        form = ContactoForm()

    return render(request, 'AppEcommerce/contacto.html', {'form': form})

# PRODUCTOS

def productos(request, id_categoria, categoria):

    if  id_categoria is not None:
        productos = Productos.objects.filter(categoria__id_categoria=id_categoria)
    else:
        productos = Productos.objects.all()

    categoria = categoria.capitalize()

    return render(request, 'AppEcommerce/productos.html', {'productos': productos, 'categoria':categoria})

def productos_todos(request):

    productos = Productos.objects.all()

    return render(request, 'AppEcommerce/productos.html', {'productos': productos, 'categoria':'Todos'})

def buscar_productos(request):
    # Obtener el término de búsqueda desde la URL
    termino_busqueda = request.GET.get('q', '')

    # Realizar la búsqueda en los campos título, marca y categoría
    productos = Productos.objects.filter(
        Q(titulo__icontains=termino_busqueda)
    )

    return render(request, 'AppEcommerce/busqueda.html', {'productos': productos, 'termino_busqueda': termino_busqueda})


@login_required
def crear_producto(request):

    if request.method == 'POST':

        form = ProductosForm(request.POST, request.FILES)

        if form.is_valid():

            producto = form.save(commit=False)
            producto.id_usuario = request.user.id
            producto.save()
            return redirect('listar_productos')
    else:

        form = ProductosForm()

    return render(request, 'AppEcommerce/crear_producto.html', {'form': form})

@login_required
def editar_producto(request, id_producto):

    producto = get_object_or_404(Productos, id_producto=id_producto)

    if request.method == 'POST':

        form = ProductosForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():

            form.save()
            return redirect('listar_productos')
    else:

        form = ProductosForm(instance=producto)

    return render(request, 'AppEcommerce/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, id_producto):

    producto = get_object_or_404(Productos, id_producto=id_producto)
    producto.delete()
    return redirect('listar_productos')

@login_required
def listar_productos(request):

    #productos = Productos.objects.all()
    #return render(request, 'AppEcommerce/listar_productos.html', {'productos': productos}).
    productos = Productos.objects.select_related('categoria', 'marca').all()
    return render(request, "AppEcommerce/productosListar.html", {'productos':productos})

@login_required    
def productosListar(request):

    productos = Productos.objects.select_related('categoria', 'marca').all()

    return render(request, "AppEcommerce/productosListar.html", {'productos':productos})
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()

    productos = Productos.objects.all()

    return render(request, "AppEcommerce/productosListar.html", {'productos':productos})  

def detalle_producto(request, id_producto):

    producto = get_object_or_404(Productos, id_producto=id_producto)
    return render(request, 'AppEcommerce/productosDetalle.html', {'producto': producto})

# /PRODUCTOS


# LOGIN + PERFIL

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contra  = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:

                login(request, user)

                messages.success(request, 'Bienvenido')
                return redirect('inicio')
            
            else:

                messages.success(request, 'Los datos ingresados no son conrrectos')
                return redirect('Login')
            
        else:
                
                messages.success(request, 'Error, formulario erroneo')
                return redirect('Login')
        
    form = AuthenticationForm()

    return render(request, "AppEcommerce/login.html", {"form":form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request, "AppEcommerce/index.html", {"mensaje":"Usuario Creado"})
        
    else:

        form = UserCreationForm()

    return render(request, "AppEcommerce/registro.html", {"form":form})            

@login_required
def mostrar_perfil(request):

    usuario = request.user
    perfil = UserProfile.objects.get_or_create(user=usuario)[0]

    return render(request, 'AppEcommerce/mostrar_perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):

    usuario = request.user
    perfil = UserProfile.objects.get_or_create(user=usuario)[0]

    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            form.save()
            return redirect('mostrar_perfil')  # Reemplazar con la URL correcta
    else:
        
        form = UserProfileForm(instance=perfil)

    return render(request, 'AppEcommerce/editar_perfil.html', {'form': form})

@login_required
def cambiar_clave(request):

    activate('es')

    if request.method == 'POST':

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)  # Actualizar la sesión para evitar el cierre de sesión
            messages.success(request, 'Tu clave ha sido cambiada correctamente.')
            return redirect('mostrar_perfil')  # Reemplazar con la URL correcta
        
        else:
            messages.error(request, 'Hubo un error al cambiar la clave. Por favor, corrige los errores.')

    else:

        form = PasswordChangeForm(request.user)

    return render(request, 'AppEcommerce/cambiar_clave.html', {'form': form})

def salir(request):

    logout(request)

    # Mensaje de éxito
    messages.success(request, 'Saliste del sistema')

    # Redireccionar a otra página
    return redirect('inicio')

# /LOGIN + PERFIL
def newsletter(request):
     
     if request.method == 'POST':
        email = request.POST.get('email')
        newsletter = Newsletter(email= email)
        newsletter.save()
        messages.success(request, 'Exito')
        return redirect('inicio')
     


