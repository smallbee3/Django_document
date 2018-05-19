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

# class ChildC(ExtraManagerModel, AbstractBase):
#   위 방법이 아니라 아래가 맞다
#   "The solution is to put the extra managers in another base class
#    and introduce it into the inheritance hierarchy after the defaults:"
# https://docs.djangoproject.com/en/2.0/topics/db/managers/#custom-managers-and-model-inheritance

class ChildC(AbstractBase, ExtraManagerModel):
    pass


class ChildD(ExtraManagerModel):
    pass


# 5.19 default manager 확인은
# ex) ChildC._default_manager
#     ChildD._default_manager
#   이런식으로 한다.
#   ChildC.objects는 참고로 default manager가 아니라
#   objects라는 이름을 가진 manager이고
#   별도의 지정(오버라이딩)이 없으면 default manager가 이 objects의 이름으로 설정된다.
