from django.db import models

# Create your models here.
class Kuzov (models.Model):
    tipkuzova = models.CharField(max_length=50)
    def __str__(self):
        return self.tipkuzova

class Marka (models.Model):    
    naim = models.CharField(max_length=50)
    def __str__(self):
        return self.naim

class ModelAuto (models.Model):    
    naimenovanie = models.CharField(max_length=50)
    izobrazhenie =  models.CharField(max_length=200, blank=True, null=True)
    photoosobennosti =  models.CharField(max_length=200, blank=True, null=True)
    photo1 =  models.CharField(max_length=200, blank=True, null=True)
    photo2 =  models.CharField(max_length=200, blank=True, null=True)
    photo3 =  models.CharField(max_length=200, blank=True, null=True)
    clirens = models.FloatField(null=True, blank=True, default=0.0)
    kolesa = models.CharField(max_length=50, blank=True, null=True)
    toplivo = models.CharField(max_length=50, blank=True, null=True)
    korobkaperedach = models.CharField(max_length=50, blank=True, null=True) 
    privod = models.CharField(max_length=50, blank=True, null=True)
    osobennosti = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    opisanie = models.TextField(blank=True, null=True)
    shirina = models.FloatField(null=True, blank=True, default=0.0)
    visota = models.FloatField(null=True, blank=True, default=0.0)
    dlina = models.FloatField(null=True, blank=True, default=0.0)
    stepensjatiya = models.FloatField(null=True, blank=True, default=0.0)
    mochnost = models.FloatField(null=True, blank=True, default=0.0)
    obembaka = models.FloatField(null=True, blank=True, default=0.0)
    kuzov = models.ForeignKey(Kuzov, on_delete=models.SET_NULL, blank=True, null=True)
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, blank=True, null=True)

    
    