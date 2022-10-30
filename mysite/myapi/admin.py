from django.contrib import admin

from .models import Wishlists
from .models import Books
from .models import Genres
from .models import Bookratings
from .models import Purchasedbooks
from .models import Addresses
from .models import Authors
from .models import Users
from .models import Creditcards
from. models import AverageRating

admin.site.register(Wishlists)
admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Bookratings)
admin.site.register(Purchasedbooks)
admin.site.register(Addresses)
admin.site.register(Authors)
admin.site.register(Users)
admin.site.register(Creditcards)
admin.site.register(AverageRating)

