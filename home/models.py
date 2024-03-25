from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Home(models.Model):
    image = models.ImageField(upload_to='home_images/')


class About(models.Model):
    image = models.ImageField(upload_to='about_images/')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')


class Versions(models.Model):
    image = models.ImageField(upload_to='versions_images/')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def  __str__(self):
        return self.name