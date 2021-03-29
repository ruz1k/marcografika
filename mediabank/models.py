from django.db import models

# Create your models here.
class PhotoMedia(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пример работ(Фото)'
        verbose_name_plural = 'Пример работ(Фото)'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class VideoMedia(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='mediabank/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Пример работ(Видео)'
        verbose_name_plural = 'Пример работ(Видео)'
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name