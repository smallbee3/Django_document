from django.db import models



class Car(models.Model):
    manufacturer = models.ForeignKey(

        'Manufacturer', # -> 문자열로 하면 참조하기 때문에 가능.
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        return f'{self.manufacturer.name} {self.name}'

class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=60)
    # 자기 자신을 다대일로 연결하는 필드
    # 비어있어도 무관, 연결된 객체가 삭제되면 함께 삭제되지 않고
    # 해당 필드를 비움
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL, # 선생이 삭제되었을 때 어떻게 할 것인지.
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.teacher:
            return f'{self.name} (teacher: {self.teacher})'
        return f'{self.name}'



# class Type(models.Model):
#     name = models.CharField(primary_key=True, max_length=60)
#
#     def __str__(self):
#         return f'{self.type_numbeer}| {self.name}'
#
#
# class Pokemon(models.Model):
#
#     dex_number = models.IntegerField(primary_key=True)
#     type = models.ForeignKey(Type, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.dex_number:03}. {self.name} (self.type.name)'