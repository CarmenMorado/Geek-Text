from django.contrib import admin
from .models import Wishlists
from .models import Books
from .models import Genres
admin.site.register(Wishlists)
admin.site.register(Books)
admin.site.register(Genres)