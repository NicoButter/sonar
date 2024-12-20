from django.urls import path
from . import views

urlpatterns = [
    path('representative/', views.representative_dashboard, name='representative_dashboard'),
    # path('admin/', views.admin_dashboard, name='admin_dashboard'),
    # path('moderator/', views.moderator_dashboard, name='moderator_dashboard'),
]
