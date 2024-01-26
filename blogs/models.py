# models.py
from django.db import models

class Lawyer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.title
