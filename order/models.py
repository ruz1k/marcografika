from django.db import models

# Create your models here.
class OrderList(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Оформить заказ(услуга)'
        verbose_name_plural = 'Оформить заказ(услуга)'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name