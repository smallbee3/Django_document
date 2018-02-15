from django.db import models


# verbose_name지정 / class Meta 에 지정할 수도 있음.


class Car(models.Model):
    manufacturer = models.ForeignKey(

        'Manufacturer', # -> 아직 정의되지 않은 모델을 참조하고 싶을 때는 문자열로 하면 알아서 찾아서 반영시킴.
        on_delete=models.CASCADE,
        verbose_name='제조사',                                 # verbose_name
        # blank=True,
        # null=True
    )
    name = models.CharField('모델명', max_length=60)            # verbose_name

    def __str__(self):
        # 현대 아반떼 <- 와 같이 출력되도록 처리
        return f'{self.manufacturer.name} {self.name}'

class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)         # verbose_name

    def __str__(self):
        return self.name






class Person(models.Model):
    name = models.CharField(max_length=60)
    #######################################################
    # Many-to-one relationships + recursive relationships #
    #######################################################
    # 1. 자기 자신을 다대일로 연결하는 필드
    # 2. 비어있어도 무관,
    # 3. 연결된 객체가 삭제되면 함께 삭제되지 않고 해당 필드를 비움
    teacher = models.ForeignKey(
        'self',                                             # <- M-t-o : recursive
        on_delete=models.SET_NULL, # 선생이 삭제되었을 때 어떻게 할 것인지.
        null=True,                 # -> models.CASCADE로 바꾸면 데이터베이스에 변동이가기때문에 pmmm해야됨.
        blank=True,
    )

    ################## 선생님이 존재할 경우에 #######################
    def __str__(self):
        if self.teacher:
            return f'{self.name} (teacher: {self.teacher})'
        return f'{self.name}'









class Type(models.Model):
    name = models.CharField(primary_key=True, max_length=60)

    def __str__(self):
        return f'{self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03}. {self.name} ({self.type.name})'