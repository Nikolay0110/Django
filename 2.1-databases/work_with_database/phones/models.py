from django.db import models
from django.urls import reverse

class Phone(models.Model):
    id = models.CharField('id', max_length=50, primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Модель')
    image = models.CharField(max_length=300, verbose_name='Изображение')
    price = models.FloatField(verbose_name='Цена')
    release_date = models.DateTimeField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

'id, name, price, image, release_date, lte_exists и slug'