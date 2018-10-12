from django.db import models
from django.db.models import Manager


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


####################################################
# 커스텀 매니저 생성 클래스
class NewManager(Manager):
    def get_queryset(self):
        print('NewManager get_queryset')
        return super().get_queryset()

####################################################


# 커스텀 매니저를 직접 자신의 속성으로 갖는 MyPerson1
class MyPerson1(Person):
    secondary = NewManager()

    class Meta:
        proxy = True


# --------------------------------------


# 커스텀 매니저를 속성으로 갖는 ABC Model
class ExtraManagerModel(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True


# 커스텀 매니저를 갖는 ABC모델을 상속받은 MyPerson2
# (간접적으로 secondary라는 Manager를 갖게됨)
class MyPerson2(Person, ExtraManagerModel):
    class Meta:
        proxy = True


class ExtraManagerModel2(models.Model):
    secondary = NewManager()

    # class Meta:
    #     abstract = True


class MyPerson3(ExtraManagerModel2):
    class Meta:
        proxy = True
