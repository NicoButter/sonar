from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Banda, ImagenBanda
from .forms import BandaForm, IntegranteForm, BiografiaForm, ImagenRepresentativaForm
import os
from django.conf import settings
from django.core.files import File
from django.core.exceptions import PermissionDenied

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
    banda = get_object_or_404(Banda, id=banda_id)  # Obtén la banda o devuelve 404 si no existe
    return render(request, 'bandas/banda_detail.html', {'banda': banda})

#--------------------------------------------------------------------------------------------------------------

@login_required
def edit_banda(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)  # Obtén la banda por ID

    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES, instance=banda)  # Asocia el formulario con la banda
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('banda_detail', banda_id=banda.id)  # Redirige a la página de detalles de la banda
    else:
        form = BandaForm(instance=banda)  # Si no es un POST, muestra el formulario con los datos de la banda

    return render(request, 'bandas/edit_banda.html', {'form': form, 'banda': banda})

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

def upload_imagen(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    # Procesar las imágenes cuando se suban
    if request.method == 'POST':
        if len(request.FILES.getlist('imagenes')) > 5:
            messages.error(request, "Solo puedes subir un máximo de 5 imágenes.")
            return redirect('upload_imagen', banda_id=banda_id)
        
        # Guardar las imágenes subidas
        for imagen in request.FILES.getlist('imagenes'):
            ImagenBanda.objects.create(banda=banda, imagen=imagen)
        
        messages.success(request, "Imágenes subidas exitosamente.")
        return redirect('upload_imagen', banda_id=banda_id)

    # Obtener las imágenes subidas previamente
    imagenes = ImagenBanda.objects.filter(banda=banda)

    return render(request, 'bandas/upload_imagen.html', {
        'banda': banda,
        'imagenes': imagenes,
    })

#--------------------------------------------------------------------------------------------------------------

def eliminar_imagen(request, imagen_id):
    imagen = ImagenBanda.objects.get(id=imagen_id)
    banda_id = imagen.banda.id
    imagen.delete()
    messages.success(request, "Imagen eliminada exitosamente.")
    return redirect('upload_imagen', banda_id=banda_id)

#--------------------------------------------------------------------------------------------------------------

@login_required
def upload_demo(request, banda_id):
    if request.method == "POST":
        banda = get_object_or_404(Banda, id=banda_id)  # Obtener la banda por su ID
        banda.demos = request.FILES['demos']
        banda.save()
        messages.success(request, "Demo subido correctamente.")
        return redirect('representative_dashboard')  # Redirigir al dashboard del representante
    else:
        messages.error(request, "Método no permitido.")
        return redirect('representative_dashboard')
    

#--------------------------------------------------------------------------------------------------------------

def editar_biografia(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    
    if request.method == 'POST':
        form = BiografiaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('banda_detail', banda_id=banda.id)  # Redirige a la vista de detalles de la banda
    else:
        form = BiografiaForm(instance=banda)

    return render(request, 'bandas/edit_biografia.html', {'form': form, 'banda': banda})

#--------------------------------------------------------------------------------------------------------------

def editar_integrantes(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)

    if request.method == 'POST':
        form = IntegranteForm(request.POST, request.FILES)
        if form.is_valid():
            integrante = form.save(commit=False)
            integrante.banda = banda
            integrante.save()
            return redirect('banda_detail', banda_id=banda.id)  # Redirige a los detalles de la banda
    else:
        form = IntegranteForm()

    return render(request, 'bandas/edit_integrantes.html', {'form': form, 'banda': banda})

#--------------------------------------------------------------------------------------------------------------

def actualizar_imagen_representativa(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        form = ImagenRepresentativaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('representative_dashboard')  # Cambia a tu nombre de vista correspondiente
    else:
        form = ImagenRepresentativaForm(instance=banda)
    return render(request, 'bandas/edit_representative_image.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------
