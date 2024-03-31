from rest_framework import generics
from apps.library.models import Book
from apps.library.api.serializers.book import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
