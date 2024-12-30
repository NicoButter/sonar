from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bandas.models import Banda, Integrante, EstiloMusical
from .forms import BandaForm, IntegranteForm
import os
from django.conf import settings
from django.core.files import File
from django.core.exceptions import PermissionDenied

#--------------------------------------------------------------------------------------------------------------

@login_required
def representative_dashboard(request):
    if not request.user.is_representative:
        return redirect('landing_page')  # Redirigir si el usuario no es representante

    # Obtener o crear la banda asociada al representante
    banda, created = Banda.objects.get_or_create(representante=request.user)

    if request.method == "POST":
        if 'add_integrante' in request.POST:
            # Agregar un integrante
            rol = request.POST['rol']
            instrumentos = request.POST['instrumentos_favoritos']
            fecha_ingreso = request.POST['fecha_ingreso']
            genero = request.POST['genero_preferido']
            descripcion = request.POST['descripcion_personal']
            Integrante.objects.create(
                banda=banda,
                rol=rol,
                instrumentos_favoritos=instrumentos,
                fecha_ingreso=fecha_ingreso,
                genero_preferido=genero,
                descripcion_personal=descripcion
            )
        elif 'upload_demo' in request.POST:
            # Subir un demo
            banda.demos = request.FILES['demos']
            banda.save()
        elif 'upload_imagen' in request.POST:
            # Subir una imagen
            banda.imagen = request.FILES['imagen']
            banda.save()

    integrantes = banda.integrantes.all()
    estilos = EstiloMusical.objects.all()

    return render(request, 'dashboard/representative_dashboard.html', {
        'banda': banda,
        'integrantes': integrantes,
        'estilos': estilos,
    })

#--------------------------------------------------------------------------------------------------------------

def banda_list(request):
    bandas = Banda.objects.all()  # Recuperar todas las bandas
    context = {'bandas': bandas}
    return render(request, 'bandas/banda_list.html', context)

#--------------------------------------------------------------------------------------------------------------

def crear_integrante(request):
    if request.method == 'POST':
        integrante_form = IntegranteForm(request.POST, request.FILES)
        if integrante_form.is_valid():
            integrante_form.save()
            return redirect('some_success_url')  # Redirige a una página de éxito o a la lista de bandas
    else:
        integrante_form = IntegranteForm()

    return render(request, 'bandas/crear_integrante.html', {'integrante_form': integrante_form})

#--------------------------------------------------------------------------------------------------------------

def banda_detail(request, banda_id):
    banda = get_object_or_404(Banda, banda_id=banda_id)  # Obtén la banda o devuelve 404 si no existe
    return render(request, 'bandas/banda_detail.html', {'banda': banda})

#--------------------------------------------------------------------------------------------------------------

def edit_banda(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)  # Usa banda_id en lugar de pk

    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()  # Guarda los cambios realizados
            return redirect('banda_detail', banda_id=banda.id)  # Redirige a los detalles de la banda
    else:
        form = BandaForm(instance=banda)

    return render(request, 'edit_banda.html', {'form': form, 'banda': banda})

#--------------------------------------------------------------------------------------------------------------

@login_required
def create_banda(request):
    if request.method == 'POST':
        # Crear un formulario solo con el nombre de la banda
        nombre_banda = request.POST.get('nombre')
        if nombre_banda:
            # Crear la banda solo con el nombre, sin el representante por ahora
            banda = Banda.objects.create(nombre=nombre_banda)
            
            # Asignar el representante al usuario logueado
            banda.representante = request.user

            # Asignar imagen por defecto
            default_image_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'no-image.png')
            with open(default_image_path, 'rb') as f:
                banda.imagen.save('no-image.png', File(f))

            banda.save()

            # Redirigir a la vista de edición para agregar más detalles
            return redirect('representative_dashboard.html')
    else:
        return render(request, 'create_banda.html')

#--------------------------------------------------------------------------------------------------------------

@login_required
def eliminar_banda(request, banda_id):
    # Obtener la banda por ID
    banda = get_object_or_404(Banda, id=banda_id)

    # Verificar que el usuario logueado sea el representante de la banda
    if banda.representante != request.user:
        raise PermissionDenied("No tienes permiso para eliminar esta banda.")

    # Eliminar la banda
    banda.delete()

    # Redirigir a la vista de dashboard del representante
    return redirect('representative_dashboard')

#--------------------------------------------------------------------------------------------------------------
