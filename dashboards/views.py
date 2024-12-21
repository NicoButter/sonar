from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Usuario

@login_required
def representative_dashboard(request):
    if not request.user.is_representative:
        return redirect('landing_page')  # Redirigir si no es representante
    
    # Lógica para cargar los datos de la banda asociada
    banda = getattr(request.user, 'banda', None)  # Obtener la banda del representante
    context = {'banda': banda}
    return render(request, 'representative_dashboard.html', context)

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('landing_page')  # Redirigir si no es administrador
    
    # Lógica específica para el dashboard del administrador
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def moderator_dashboard(request):
    if not request.user.is_moderator:
        return redirect('landing_page')  # Redirigir si no es moderador
    
    # Lógica específica para el dashboard del moderador
    return render(request, 'dashboard/moderator_dashboard.html')
