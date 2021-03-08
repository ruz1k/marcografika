from django.conf import settings
from django.db import models

class Service(models.Model):
    service = models.CharField(max_length=200)
    service_title = models.CharField(max_length=200)
    service_text = models.TextField()
    service_image = models.ImageField(upload_to="media/uslugi", null=True)
    price = models.IntegerField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title