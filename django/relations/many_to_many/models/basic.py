from django.db import models


__all__ = (
    'Topping',
    'Pizza',
)

# 뭐죠? 그냥 특정한것들만 불러오고. 나머지는 안불러오고 싶을 때
# 내부적으로만 쓰는 함수가 있으면 같이 들어가버리니까.
# 이름이 꼬여버리면 함수이름이 겹쳐진다거나 하면 문제가
#


class Topping(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Basic - Toppings'
        # plural 안 붙이면 s 가 하나 더 붙음.

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    class Meta:
        verbose_name_plural = 'Basic - Pizzas'

    def __str__(self):
        return self.name


