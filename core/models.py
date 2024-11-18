from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class DateTimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Site(models.Model):
    name = models.CharField(max_length=100)
    about_us = models.TextField(default="", null=True, blank=True)
    address = models.TextField(default="", null=True, blank=True)
    header_image = CloudinaryField(folder="site/", null=True, blank=True)
    header_title = models.CharField(max_length=100, default="", null=True, blank=True)
    phone_number = models.CharField(
        max_length=20,
        default="",
        null=True,
        blank=True,
        help_text="Phone number with country code i.e. 917990577979",
    )
    email = models.EmailField(default="", null=True, blank=True)
    facebook = models.URLField(default="", null=True, blank=True)
    instagram = models.URLField(default="", null=True, blank=True)
    youtube = models.URLField(default="", null=True, blank=True)
    google_maps = models.URLField(default="", null=True, blank=True)

    def __str__(self):
        return self.name


class Gallery(DateTimeBaseModel):
    image = CloudinaryField(folder="gallery/")
    title = models.CharField(max_length=100, default="", null=True, blank=True)
    index_order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["index_order"]
        

class Course(DateTimeBaseModel):
    image = CloudinaryField(folder="gallery/", null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default="", null=True, blank=True)
    index_order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["index_order"]


class Team(DateTimeBaseModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = CloudinaryField(folder="team/")
    index_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["index_order"]


class Client(DateTimeBaseModel):
    name = models.CharField(max_length=100)
    comment = models.TextField(default="", null=True, blank=True)
    image = CloudinaryField(folder="clients/")
    index_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["index_order"]
