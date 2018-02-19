from django.db import models
from django.db.models.manager import BaseManager, Manager


class User(models.Model):
    name = models.CharField(max_length=50)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name

####################################################
# 커스텀 매니저 생성 클래스
class AdminManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)
###################################################

class Admin(User):
    secondary = AdminManager()

    class Meta:
        proxy = True


    def __str__(self):
        return f'{self.name} (관리자)'

    @staticmethod
    def drop(user):
        user.delete()

# 여기서 Manager와 커스텀 매니저인 Admin


####################################################
# 커스텀 매니저 생성 클래스
class StaffManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)
###################################################


class Staff(User):
    secondary = StaffManager()
    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (스태프)'

    @staticmethod
    def block(user):
        user.is_block = True
        user.save()