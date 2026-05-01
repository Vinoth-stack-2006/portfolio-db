from django import forms
from .models import ContactMessage, Project, Skill, Experience, Profile

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'your@email.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your message...', 'rows': 5}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'long_description', 'tech_stack', 'github_url', 'live_url', 'image', 'status', 'featured', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'dash-input'}),
            'description': forms.Textarea(attrs={'class': 'dash-textarea', 'rows': 3}),
            'long_description': forms.Textarea(attrs={'class': 'dash-textarea', 'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Python, Django, Docker, AWS'}),
            'github_url': forms.URLInput(attrs={'class': 'dash-input'}),
            'live_url': forms.URLInput(attrs={'class': 'dash-input'}),
            'status': forms.Select(attrs={'class': 'dash-select'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'proficiency', 'icon', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'category': forms.Select(attrs={'class': 'dash-select'}),
            'proficiency': forms.NumberInput(attrs={'class': 'dash-input', 'min': 0, 'max': 100}),
            'icon': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'devicon-python-plain'}),
            'order': forms.NumberInput(attrs={'class': 'dash-input'}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'role', 'start_date', 'end_date', 'is_current', 'description', 'tech_used', 'location']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'dash-input'}),
            'role': forms.TextInput(attrs={'class': 'dash-input'}),
            'start_date': forms.DateInput(attrs={'class': 'dash-input', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'dash-input', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'dash-textarea', 'rows': 4}),
            'tech_used': forms.TextInput(attrs={'class': 'dash-input', 'placeholder': 'Python, AWS, Kubernetes'}),
            'location': forms.TextInput(attrs={'class': 'dash-input'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'bio', 'email', 'github', 'linkedin', 'location', 'years_experience', 'resume']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'dash-input'}),
            'title': forms.TextInput(attrs={'class': 'dash-input'}),
            'bio': forms.Textarea(attrs={'class': 'dash-textarea', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'dash-input'}),
            'github': forms.URLInput(attrs={'class': 'dash-input'}),
            'linkedin': forms.URLInput(attrs={'class': 'dash-input'}),
            'location': forms.TextInput(attrs={'class': 'dash-input'}),
            'years_experience': forms.NumberInput(attrs={'class': 'dash-input'}),
        }
