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
        related_name='%(app_label)s_%(class)s_set',
        # related_query_name='%(app_label)s_%(class)s',

        related_query_name='bases',
        # -> 컴파일 에러가 나지 않아서 아무 문제가 나지 않는 것처럼 보이지만
        #    실제로는 두 sub_class가 위의 'bases'를 related_query_name으로
        #    동일하게 같게 되면서 데이터가 꼬이는 문제가 발생하게 된다.
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
