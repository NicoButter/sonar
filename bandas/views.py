"""Vistas de la aplicación bandas.

Contiene las vistas para listar, crear, editar, eliminar bandas,
gestionar imágenes, demos, biografías e integrantes.
"""

import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.files import File
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    BandaForm,
    BiografiaForm,
    ImagenRepresentativaForm,
    IntegranteForm,
)
from .models import Banda, ImagenBanda


# ---------------------------------------------------------------------------
# Listado y detalle
# ---------------------------------------------------------------------------

def banda_list(request):
    """Lista todas las bandas registradas.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el listado de bandas.
    """
    bandas = Banda.objects.all()
    context = {'bandas': bandas}
    return render(request, 'bandas/banda_list.html', context)


def banda_detail(request, banda_id):
    """Muestra el detalle de una banda específica.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a consultar.

    Returns:
        HttpResponse con el detalle de la banda, o 404 si no existe.
    """
    banda = get_object_or_404(Banda, id=banda_id)
    return render(request, 'bandas/banda_detail.html', {'banda': banda})


# ---------------------------------------------------------------------------
# Creación y edición
# ---------------------------------------------------------------------------

@login_required
def crear_integrante(request):
    """Crea un nuevo integrante mediante un formulario.

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el formulario o redirección tras crear.
    """
    if request.method == 'POST':
        integrante_form = IntegranteForm(request.POST, request.FILES)
        if integrante_form.is_valid():
            integrante_form.save()
            return redirect('some_success_url')
    else:
        integrante_form = IntegranteForm()

    return render(
        request, 'bandas/crear_integrante.html',
        {'integrante_form': integrante_form},
    )


@login_required
def edit_banda(request, banda_id):
    """Edita los datos de una banda existente.

    Requiere autenticación. Muestra un formulario con los datos
    actuales de la banda y guarda los cambios al enviar.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a editar.

    Returns:
        HttpResponse con el formulario de edición o redirección
        al detalle de la banda tras guardar.
    """
    banda = get_object_or_404(Banda, id=banda_id)

    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('banda_detail', banda_id=banda.id)
    else:
        form = BandaForm(instance=banda)

    return render(
        request, 'bandas/edit_banda.html', {'form': form, 'banda': banda},
    )


@login_required
def create_banda(request):
    """Crea una nueva banda asociada al usuario autenticado.

    Genera la banda solo con el nombre, asigna al usuario actual
    como representante y establece una imagen por defecto.

    Args:
        request: Objeto HttpRequest de Django.

    Returns:
        HttpResponse con el formulario de creación o redirección
        al dashboard del representante.
    """
    if request.method == 'POST':
        nombre_banda = request.POST.get('nombre')
        if nombre_banda:
            banda = Banda.objects.create(nombre=nombre_banda)
            banda.representante = request.user

            default_image_path = os.path.join(
                settings.BASE_DIR, 'static', 'images', 'no-image.png',
            )
            with open(default_image_path, 'rb') as f:
                banda.imagen.save('no-image.png', File(f))

            banda.save()
            return redirect('representative_dashboard')
    else:
        return render(request, 'bandas/create_banda.html')


# ---------------------------------------------------------------------------
# Eliminación
# ---------------------------------------------------------------------------

@login_required
def eliminar_banda(request, banda_id):
    """Elimina una banda si el usuario es su representante.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a eliminar.

    Returns:
        HttpResponseRedirect al dashboard del representante.

    Raises:
        PermissionDenied: Si el usuario no es el representante de la banda.
    """
    banda = get_object_or_404(Banda, id=banda_id)

    if banda.representante != request.user:
        raise PermissionDenied("No tienes permiso para eliminar esta banda.")

    banda.delete()
    return redirect('representative_dashboard')


# ---------------------------------------------------------------------------
# Gestión de imágenes
# ---------------------------------------------------------------------------

@login_required
def upload_imagen(request, banda_id):
    """Sube imágenes adicionales para una banda (máximo 5).

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda destino.

    Returns:
        HttpResponse con el formulario de subida y las imágenes existentes.
    """
    banda = Banda.objects.get(id=banda_id)

    if request.method == 'POST':
        if len(request.FILES.getlist('imagenes')) > 5:
            messages.error(
                request, "Solo puedes subir un máximo de 5 imágenes.",
            )
            return redirect('upload_imagen', banda_id=banda_id)

        for imagen in request.FILES.getlist('imagenes'):
            ImagenBanda.objects.create(banda=banda, imagen=imagen)

        messages.success(request, "Imágenes subidas exitosamente.")
        return redirect('upload_imagen', banda_id=banda_id)

    imagenes = ImagenBanda.objects.filter(banda=banda)
    return render(request, 'bandas/upload_imagen.html', {
        'banda': banda,
        'imagenes': imagenes,
    })


@login_required
def eliminar_imagen(request, imagen_id):
    """Elimina una imagen de la galería de una banda.

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.
        imagen_id: ID de la imagen a eliminar.

    Returns:
        HttpResponseRedirect a la vista de subida de imágenes.
    """
    imagen = ImagenBanda.objects.get(id=imagen_id)
    banda_id = imagen.banda.id
    imagen.delete()
    messages.success(request, "Imagen eliminada exitosamente.")
    return redirect('upload_imagen', banda_id=banda_id)


@login_required
def actualizar_imagen_representativa(request, banda_id):
    """Actualiza la imagen representativa de una banda.

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a actualizar.

    Returns:
        HttpResponse con el formulario o redirección tras guardar.
    """
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        form = ImagenRepresentativaForm(
            request.POST, request.FILES, instance=banda,
        )
        if form.is_valid():
            form.save()
            return redirect('representative_dashboard')
    else:
        form = ImagenRepresentativaForm(instance=banda)
    return render(
        request, 'bandas/edit_representative_image.html', {'form': form},
    )


# ---------------------------------------------------------------------------
# Demos
# ---------------------------------------------------------------------------

@login_required
def upload_demo(request, banda_id):
    """Sube un archivo de demo para una banda.

    Solo acepta el método POST. El archivo se asocia a la banda
    indicada por ``banda_id``.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda destino.

    Returns:
        HttpResponseRedirect al dashboard del representante.
    """
    if request.method == "POST":
        banda = get_object_or_404(Banda, id=banda_id)
        banda.demos = request.FILES['demos']
        banda.save()
        messages.success(request, "Demo subido correctamente.")
        return redirect('representative_dashboard')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('representative_dashboard')


# ---------------------------------------------------------------------------
# Biografía e integrantes
# ---------------------------------------------------------------------------

@login_required
def editar_biografia(request, banda_id):
    """Edita la biografía de una banda.

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a editar.

    Returns:
        HttpResponse con el formulario de edición o redirección
        al detalle de la banda tras guardar.
    """
    banda = get_object_or_404(Banda, id=banda_id)

    if request.method == 'POST':
        form = BiografiaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('banda_detail', banda_id=banda.id)
    else:
        form = BiografiaForm(instance=banda)

    return render(
        request, 'bandas/edit_biografia.html',
        {'form': form, 'banda': banda},
    )


@login_required
def editar_integrantes(request, banda_id):
    """Agrega un nuevo integrante a una banda.

    Requiere autenticación.

    Args:
        request: Objeto HttpRequest de Django.
        banda_id: ID de la banda a la que se agrega el integrante.

    Returns:
        HttpResponse con el formulario o redirección al detalle
        de la banda tras guardar.
    """
    banda = get_object_or_404(Banda, id=banda_id)

    if request.method == 'POST':
        form = IntegranteForm(request.POST, request.FILES)
        if form.is_valid():
            integrante = form.save(commit=False)
            integrante.banda = banda
            integrante.save()
            return redirect('banda_detail', banda_id=banda.id)
    else:
        form = IntegranteForm()

    return render(
        request, 'bandas/edit_integrantes.html',
        {'form': form, 'banda': banda},
    )
