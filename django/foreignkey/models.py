from django.db import models

class Manufacturer(models.Model):
    # ...
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        return f'{self.manufacturer.name} {self.name}'
