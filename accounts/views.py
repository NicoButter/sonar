from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def landing_page(request):
    return render(request, 'landing_page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Redirigir al dashboard según el rol del usuario
            if user.is_representative:
                return redirect(reverse('representative_dashboard'))
            elif user.is_admin:
                return redirect(reverse('admin_dashboard'))
            elif user.is_moderator:
                return redirect(reverse('moderator_dashboard'))
            else:
                return redirect('landing_page')  # Visitante u otro caso
            
        else:
            # Manejar error de autenticación
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('landing_page')
