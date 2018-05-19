from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,

        # 아래 선언을 하지 않으니 아래 상속받은 자식들에
        # 역참조 및 역참조쿼리를 사용할 수 없다.

        # related_name='items',

        # related_query_name의 경우 컴파일에러를 파이참이 발생시키지 않는데
        # 사실 related_name = 'items'처럼 문제가 되며,
        # 나중에 지정된 related_query_name으로 뒤집어 쓰게 된다.

        related_query_name='item',

        related_name='%(app_label)s_%(class)ss',
        # related_query_name='%(app_label)s_%(class)s',
        # 역참조 쿼리 네임을 지정하지 않으면 related_name을 따라간다.
    )

    class Meta:
        abstract = True


class Fruit(Item):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Food(Item):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name