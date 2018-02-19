from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'Place {self.name} | {self.address}'



class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    # nearby_places = models.ManyToManyField(
    #     Place,
    #     related_query_name='near_restaurant'
    # )

    def __str__(self):
        return f'Restaurant {self.name}'

# Adding related_name to the customers field
# as follows would resolve the error: models.ManyToManyField(Place, related_name='provider').

class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

    def __str__(self):
        return f'Supplier {self.customers} of {self.name}'