from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    is_block = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Admin(User):
    class Meta:
        proxy = True

    def drop(self, user):
        user.delete()


class Staff(User):
    class Meta:
        proxy = True

    def block(self, user):
        user.is_block = True
        user.save()