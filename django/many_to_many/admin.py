from django.contrib import admin

from .models import *

admin.site.register(Topping)
admin.site.register(Pizza)


admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(User)