from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    years_experience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume/', blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('database', 'Database'),
        ('tools', 'Tools'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(default=80, help_text="0-100 percentage")
    icon = models.CharField(max_length=100, blank=True, help_text="Devicon class e.g. devicon-python-plain")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'category']

    def __str__(self):
        return f"{self.name} ({self.category})"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    tech_used = models.CharField(max_length=500, blank=True, help_text="Comma-separated technologies")
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} @ {self.company}"

class Project(models.Model):
    STATUS_CHOICES = [
        ('live', 'Live'),
        ('wip', 'Work in Progress'),
        ('archived', 'Archived'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated e.g. Python, Django, Docker")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='live')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
