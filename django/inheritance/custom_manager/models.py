from django.db import models
from django.db.models import Manager


class CustomManager(Manager):
    pass



class AbstractBase(models.Model):
    objects = CustomManager()


    class Meta:
        abstract = True