from rest_framework.pagination import LimitOffsetPagination


class BookListPagination(LimitOffsetPagination):
    default_limit = 3
