from django.contrib import admin
from .models import Wishlists
from .models import Addresses
from .models import Authors

admin.site.register(Wishlists)
admin.site.register(Addresses)
admin.site.register(Authors)

