from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ServiceModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    active = models.CharField(
        max_length=200, null=True, blank=True, default='No')
    description = models.TextField(blank=True)
    sub_desction = models.TextField(blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    detailed_description = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class SummarisedServiceModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class GalleryModel(models.Model):
    group = models.CharField(max_length=200, null=True, blank=True)
    imageHero = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image1 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image2 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image3 = models.ImageField(
        null=True, blank=True, upload_to='static/images')
    image4 = models.ImageField(
        null=True, blank=True, upload_to='static/images')

    def __str__(self):
        return self.group
