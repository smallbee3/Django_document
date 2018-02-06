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
    TwitterUser, Relation
)


admin.site.register(Topping)
admin.site.register(Pizza)


admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(User)

admin.site.register(FacebookUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)