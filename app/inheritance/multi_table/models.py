from django.db import models


# 상원님을 위한 특별 예제 1
class Other(models.Model):
    pass


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    # 상원님을 위한 특별 예제 1
    # other = models.ForeignKey(
    #     Other, on_delete=models.SET_NULL, blank=True, null=True
    # )

    def __str__(self):
        return f'Place {self.name} | {self.address}'


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    # 상원님을 위한 특별 예제 2 (사실 이 부분 Doc에 설명이 있음)
    # https://docs.djangoproject.com/en/2.0/topics/db/models/#inheritance-and-reverse-relations

    nearby_places = models.ManyToManyField(
        Place,
        related_query_name='near_restaurant'
    )

    def __str__(self):
        return f'Restaurant {self.name}'

# Adding related_name to the customers field
# as follows would resolve the error: models.ManyToManyField(Place, related_name='provider').


class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

    def __str__(self):
        return f'Supplier {self.customers} of {self.name}'