from django.db import models


class Contect(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length=40)
    number = models.CharField(max_length=13)
    contect = models.TextField(max_length=400)



class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=100, help_text="Font Awesome icon class, e.g., 'fa-solid fa-code'")
    
    technologies = models.ManyToManyField(Technology, related_name="projects")

    def __str__(self):
        return self.name