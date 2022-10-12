
# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Wishlists', views.WishlistsViewSet, 'Wishlists')
router.register(r'Addresses', views.AddressesViewSet, 'Addresses')
router.register(r'Authors', views.AuthorsViewSet, 'Authors')
router.register(r'Books', views.BooksViewSet, 'Books')
router.register(r'Genres', views.GenresViewSet, 'Genres')
router.register(r'Bookratings', views.BookratingsViewSet, 'Bookratings')
router.register(r'Purchasedbooks', views.PurchasedbooksViewSet, 'Purchasedbooks')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]

    
