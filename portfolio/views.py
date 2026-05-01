from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Profile, Skill, Experience, Project, ContactMessage
from .forms import ContactForm, ProjectForm, SkillForm, ExperienceForm, ProfileForm

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    contact_form = ContactForm()

    # Group skills by category
    skill_categories = {}
    for skill in skills:
        cat = skill.get_category_display()
        if cat not in skill_categories:
            skill_categories[cat] = []
        skill_categories[cat].append(skill)

    context = {
        'profile': profile,
        'projects': projects,
        'featured_projects': featured_projects,
        'skills': skills,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'contact_form': contact_form,
    }
    return render(request, 'portfolio/home.html', context)

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors})
    return redirect('home')

def admin_login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials or insufficient permissions.')
    return render(request, 'portfolio/login.html')

def admin_logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    context = {
        'projects_count': Project.objects.count(),
        'skills_count': Skill.objects.count(),
        'experience_count': Experience.objects.count(),
        'messages_count': ContactMessage.objects.filter(is_read=False).count(),
        'recent_messages': ContactMessage.objects.all()[:5],
        'recent_projects': Project.objects.all()[:5],
    }
    return render(request, 'portfolio/dashboard.html', context)

# --- PROJECTS CRUD ---
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/crud/project_list.html', {'projects': projects})

@login_required
def project_add(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Project added successfully!')
        return redirect('project_list')
    return render(request, 'portfolio/crud/project_form.html', {'form': form, 'action': 'Add'})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Project updated!')
        return redirect('project_list')
    return render(request, 'portfolio/crud/project_form.html', {'form': form, 'action': 'Edit'})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted!')
        return redirect('project_list')
    return render(request, 'portfolio/crud/confirm_delete.html', {'obj': project, 'type': 'Project'})

# --- SKILLS CRUD ---
@login_required
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/crud/skill_list.html', {'skills': skills})

@login_required
def skill_add(request):
    form = SkillForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Skill added!')
        return redirect('skill_list')
    return render(request, 'portfolio/crud/skill_form.html', {'form': form, 'action': 'Add'})

@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = SkillForm(request.POST or None, instance=skill)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Skill updated!')
        return redirect('skill_list')
    return render(request, 'portfolio/crud/skill_form.html', {'form': form, 'action': 'Edit'})

@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted!')
        return redirect('skill_list')
    return render(request, 'portfolio/crud/confirm_delete.html', {'obj': skill, 'type': 'Skill'})

# --- EXPERIENCE CRUD ---
@login_required
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/crud/experience_list.html', {'experiences': experiences})

@login_required
def experience_add(request):
    form = ExperienceForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Experience added!')
        return redirect('experience_list')
    return render(request, 'portfolio/crud/experience_form.html', {'form': form, 'action': 'Add'})

@login_required
def experience_edit(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    form = ExperienceForm(request.POST or None, instance=exp)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Experience updated!')
        return redirect('experience_list')
    return render(request, 'portfolio/crud/experience_form.html', {'form': form, 'action': 'Edit'})

@login_required
def experience_delete(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        exp.delete()
        messages.success(request, 'Experience deleted!')
        return redirect('experience_list')
    return render(request, 'portfolio/crud/confirm_delete.html', {'obj': exp, 'type': 'Experience'})

# --- PROFILE ---
@login_required
def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Profile updated!')
        return redirect('dashboard')
    return render(request, 'portfolio/crud/profile_form.html', {'form': form})

# --- MESSAGES ---
@login_required
def message_list(request):
    msgs = ContactMessage.objects.all()
    ContactMessage.objects.filter(is_read=False).update(is_read=True)
    return render(request, 'portfolio/crud/message_list.html', {'messages_list': msgs})
