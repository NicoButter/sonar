from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bandas.models import Banda, Integrante, EstiloMusical
from .forms import BandaForm

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

@login_required
def create_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banda_list')  # Redirige a la lista de bandas después de crearla
    else:
        form = BandaForm()
    return render(request, 'bandas/create_banda.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------

def banda_detail(request, pk):
    banda = get_object_or_404(Banda, pk=pk)  # Obtén la banda o devuelve 404 si no existe
    return render(request, 'bandas/banda_detail.html', {'banda': banda})

def edit_banda(request, pk):
    banda = get_object_or_404(Banda, pk=pk)  # Obtén la banda a editar

    if request.method == "POST":
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()  # Guarda los cambios realizados
            return redirect('banda_detail', pk=banda.pk)  # Redirige a los detalles de la banda
    else:
        form = BandaForm(instance=banda)

    return render(request, 'bandas/edit_banda.html', {'form': form, 'banda': banda})