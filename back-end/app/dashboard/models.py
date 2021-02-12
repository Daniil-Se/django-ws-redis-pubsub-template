from django.db import models

# Create your models here.


class TestModel(models.Model):
    """Основная информация"""
    test = models.IntegerField('Номер test')
