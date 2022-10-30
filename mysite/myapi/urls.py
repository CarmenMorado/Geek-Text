# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from myapi.views import TopSellingBooksViewSet
from myapi.views import GenreListsViewSet
from myapi.views import TopRatedBooksViewSet
from myapi.views import AverageRatingViewSet

router = routers.DefaultRouter()
router.register(r'Wishlists', views.WishlistsViewSet, 'Wishlists')
router.register(r'Addresses', views.AddressesViewSet, 'Addresses')
router.register(r'Authors', views.AuthorsViewSet, 'Authors')
router.register(r'Books', views.BooksViewSet, 'Books')
router.register(r'Genres', views.GenresViewSet, 'Genres')
router.register(r'Bookratings', views.BookratingsViewSet, 'Bookratings')
router.register(r'Purchasedbooks', views.PurchasedbooksViewSet, 'Purchasedbooks')
router.register(r'Users', views.UsersViewSet, 'Users')
router.register(r'Creditcards', views.CreditcardsViewSet, 'Creditcards')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Books/TopSellers/', TopSellingBooksViewSet.as_view()),
    path('Books/Genre/', GenreListsViewSet.as_view()),
    path('Bookratings/TopRated/', TopRatedBooksViewSet.as_view()),
    path('Bookratings/AverageRating/', AverageRatingViewSet.as_view()),
    path('', include(router.urls))

]
