from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import MagicMock, patch
from apps.library.api.views.book import BookListCreateView
from apps.library.api.serializers.book import BookSerializer
from apps.library.models import Book
from apps.library.test.unit.factories import BookFactory
from faker import Faker

fake = Faker("pt_BR")


class TestBookAListCreateView(APITestCase):
    def setUp(self):
        self.view = BookListCreateView()

    def test_list_book_return_200(self):
        books = BookFactory.build_batch(5)
        self.view.get_queryset = MagicMock(return_value=Book.objects.all())
        mock_book_serializer = MagicMock(spec=BookSerializer)
        mock_book_serializer.data = BookSerializer(books, many=True).data
        self.view.get_serializer = MagicMock(return_value=mock_book_serializer)
        response = self.view.get(None)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_book_return_correte_data(self):
        books = BookFactory.build_batch(5)
        self.view.get_queryset = MagicMock(return_value=Book.objects.all())
        mock_book_serializer = MagicMock(spec=BookSerializer)
        mock_book_serializer.data = BookSerializer(books, many=True).data
        self.view.get_serializer = MagicMock(return_value=mock_book_serializer)
        response = self.view.get(None)
        self.assertEqual(response.data, mock_book_serializer.data)


class BookCreateTests(APITestCase):

    def test_create_book_return_201(self):
        url = reverse('library:library-api')
        data = {
            "title": fake.word(),
            "description": fake.word(),
            "pages": fake.random_int(min=50, max=1000),
            "author": fake.name(),
            "created_at": fake.date_time_between(start_date="-1y", end_date="now"),
            "updated_at": fake.date_time_between(start_date="-1y", end_date="now")
        }
        with patch('apps.library.models.Book.save'):
            response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
