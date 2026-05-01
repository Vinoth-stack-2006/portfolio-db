from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-logout/', views.admin_logout_view, name='admin_logout'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/profile/', views.profile_edit, name='profile_edit'),
    path('dashboard/messages/', views.message_list, name='message_list'),
    
    # Projects
    path('dashboard/projects/', views.project_list, name='project_list'),
    path('dashboard/projects/add/', views.project_add, name='project_add'),
    path('dashboard/projects/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('dashboard/projects/<int:pk>/delete/', views.project_delete, name='project_delete'),
    
    # Skills
    path('dashboard/skills/', views.skill_list, name='skill_list'),
    path('dashboard/skills/add/', views.skill_add, name='skill_add'),
    path('dashboard/skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('dashboard/skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    
    # Experience
    path('dashboard/experience/', views.experience_list, name='experience_list'),
    path('dashboard/experience/add/', views.experience_add, name='experience_add'),
    path('dashboard/experience/<int:pk>/edit/', views.experience_edit, name='experience_edit'),
    path('dashboard/experience/<int:pk>/delete/', views.experience_delete, name='experience_delete'),
]
