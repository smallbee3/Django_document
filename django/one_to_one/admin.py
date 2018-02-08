from django.contrib import admin

from .models import *
# from .models import Restaurant, Place, Waiter


admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)