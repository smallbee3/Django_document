from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


# Be careful with related_name and related_query_name

class Other(models.Model):
    pass


class Base(models.Model):
    other = models.ForeignKey(
        Other,
        on_delete=models.CASCADE,
        # related_name='base',

        # 3/11 복습 시간 안그래도 오래걸리는데 여기서 또 발목잡힘.
        # related_name을 선언을 아예 안하면 문제가 없는데
        #
        # 여기서는 childa_set / childb_set으로 참조가능하니 문제가안됨.
        #
        # related_name='%(app_label)s_%(class)s_set',
        # related_query_name='bases',
        # related_query_name='%(app_label)s_%(class)s',
    )

    class Meta:
        abstract = True


class ChildA(Base):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class ChildB(Base):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
