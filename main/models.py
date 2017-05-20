#-*- coding: utf-8 -*-
from django.db import models

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre_pais
    def __unicode__(self):
        return self.nombre_pais

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=25)
    pais = models.ManyToManyField(Pais)

    def __str__(self):
        return self.nombre_ciudad
    def __unicode__(self):
        return self.nombre_ciudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Foodpark(models.Model):
    nombre_foodpark = models.CharField(max_length=25)
    descripcion_foodpark = models.CharField(max_length=240)
    ciudad = models.ManyToManyField(Ciudad)
    direccion_foodpark = models.CharField(max_length=150)
    lon_foodpark = models.CharField(max_length=25)
    lat_foodpark = models.CharField(max_length=25)
    logo = models.FileField()
    telefono = models.CharField(max_length=25)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    es_favorito = models.BooleanField(default=False)
    descripcion_corta = models.CharField(max_length=240,default='Descripcion Corta')

    def __str__(self):
        return self.nombre_foodpark

    def __unicode__(self):
        return self.nombre_foodpark

    class Meta:
        verbose_name = "Foodpark"
        verbose_name_plural = "Foodparks"

class Local(models.Model):
    nombre_local = models.CharField(max_length=25)
    foodpark = models.ManyToManyField(Foodpark)
    foto_local = models.FileField()
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    es_recomendado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_local

    def __unicode__(self):
        return self.nombre_local

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locales"

class Plato(models.Model):
    nombre_plato = models.CharField(max_length=25)
    descripcion_plato = models.CharField(max_length=240)
    ingredientes_plato = models.CharField(max_length=240)
    precio = models.CharField(max_length=25)
    local = models.ManyToManyField(Local)
    foto_plato = models.FileField()

    def __str__(self):
        return self.nombre_plato

    def __unicode__(self):
        return self.nombre_plato

    class Meta:
        verbose_name = "Plato"
        verbose_name_plural = "Platos"