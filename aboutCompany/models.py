from django.db import models

# Create your models here.
class MainInfo(models.Model):
    image = models.ImageField(upload_to='about-us/main-info/%Y/%m/%d', blank=True)
    information = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Основная информация'
        verbose_name_plural = 'Основная информация'

    def __str__(self):
        return self.information

class Technologies(models.Model):
    image = models.ImageField(upload_to='about-us/technologies/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Технологии'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.name

class Clients(models.Model):
    partner_image = models.ImageField(upload_to='about-us/partners/%Y/%m/%d', blank=True)
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
