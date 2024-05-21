# models.py

from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    # Add any other fields as needed

    def __str__(self):
        return self.title

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    # Add any other fields as needed

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    # Add any other fields as needed

    def __str__(self):
        return self.title

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # Assuming phone number will be stored as a string
    city = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
