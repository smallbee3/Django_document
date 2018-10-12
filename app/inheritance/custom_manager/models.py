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
    pass


# 3. Extra model을 통해 커스텀 매니저를 지정한 상속모델
class ExtraManagerModel(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraManagerModel):
    pass


# 4. 3에서 inheritance sequence 바꾸기
#   아래 방법이 아니라 위 방법이 맞다
#   "The solution is to put the extra managers in another base class
#    and introduce it into the inheritance hierarchy after the defaults:"
# https://docs.djangoproject.com/en/2.0/topics/db/managers/#custom-managers-and-model-inheritance

class ChildD(ExtraManagerModel, AbstractBase):
    pass


# 5. 이상한 놈
class ChildE(ExtraManagerModel):
    pass


# 180519
# default manager 확인은
# ChildC._default_manager
# ChildD._default_manager
# 이런식으로 한다.
#
# * 별도의 지정(오버라이딩)이 없으면 default manager가 이 'objects'라는 이름으로 설정된다.


# 181012
# * childE 때문에 알게된 이상한 사실
# abstract class를 상속받은 sub class에서 custom manager를 만들기만 하면
# 기존의 objects가 존재하지 않는다.
# (수차례 테스트 결과 'abstract=True'나 원래 기존에 있었던 'proxy=True와도 관련이 없다.)

# 결론 : 원래 manager를 선언한 base class를 상속한 sub class에서는
# 기존의 objects manager는 더이상 호출할 수 없는 듯 하다.
