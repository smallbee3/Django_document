from django.db import models
from django.db.models import Manager


####################################################
# 커스텀 매니저 생성 클래스 1
class CustomManager(Manager):
    def get_queryset(self):
        print('Custom manager get_queryset!')
        return super().get_queryset()

# 커스텀 매니저 생성 클래스 2
class OtherManager(Manager):
    def get_queryset(self):
        print('Other manager get_queryset!')
        return super().get_queryset()
####################################################


# 부모모델
class AbstractBase(models.Model):
    objects = CustomManager()

    class Meta:
        abstract = True


# 1. 일반 상속모델
class ChildA(AbstractBase):
    pass


# 2. 커스텀 매니저를 지정한 상속모델
class ChildB(AbstractBase):
    default_manager = OtherManager()



class ExtraManagerModel(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True

# 3. Extra model을 통해 커스텀 매니저를 지정한 상속모델
class ChildC(ExtraManagerModel, AbstractBase):
    pass


class ChildD(ExtraManagerModel):
    pass