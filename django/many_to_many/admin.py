from django.contrib import admin

from .models import (
    # basic
    Topping, Pizza,
    # intermediate
    Post, User, PostLike,
    # self
    FacebookUser,
    # symmetrical
    InstagramUser,
    # symmetrical-intermediate
    TwitterUser, Relation,
)

# from .models import *

# from many_to_many.models.self import FacebookUser


admin.site.register(Topping)
admin.site.register(Pizza)

admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)

admin.site.register(FacebookUser)
admin.site.register(TwitterUser)
admin.site.register(Relation)