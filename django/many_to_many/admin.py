# from django.contrib import admin
#
# from many_to_many.models.self import FacebookUser
# from .models import *
#

from django.contrib import admin

# from many_to_many.models.self import FacebookUser
from .models import (
    # basic
    Topping, Pizza,
    # intermediate
    Post, User, PostLike,
    # self
    FacebookUser,
)


admin.site.register(Topping)
admin.site.register(Pizza)


admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(User)

admin.site.register(FacebookUser)