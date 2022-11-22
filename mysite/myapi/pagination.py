from rest_framework.pagination import LimitOffsetPagination

# class for offset pagination for the book list
class BookListPagination(LimitOffsetPagination):
    default_limit = 3 # sets the default number of books returned
