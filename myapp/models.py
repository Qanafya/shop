from django.db import models
from django.urls import reverse

# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ver_pass = models.CharField(max_length=200)


class Products(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    price = models.IntegerField()
    foto = models.CharField(max_length=200)


class Cart(models.Model):
    foto = models.CharField(max_length=200)
    pr_id = models.IntegerField()
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()

class Details(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    details = models.CharField(max_length=200)
    foto1 = models.CharField(max_length=200)
    foto2 = models.CharField(max_length=200)
    foto3 = models.CharField(max_length=200)
    foto4 = models.CharField(max_length=200)

class Comments(models.Model):
    to_id = models.IntegerField()
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

class Admins(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})


