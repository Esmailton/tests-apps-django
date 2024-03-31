from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import MagicMock
from apps.library.api.views.book import BookListCreateView
from apps.library.api.serializers.book import BookSerializer
from apps.library.models import Book
from apps.library.test.unit.factories import BookFactory


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

    def test_create_book_return_201(self):
        book_data = {
            "title": "Test Book",
            "description": "Test Description",
            "pages": 100,
            "author": "Test Author",
            "status": 1
        }

        request_factory = APIRequestFactory()
        _request = request_factory.post(
            '/api/book/', data=book_data, format='json')

        mock_book_serializer = MagicMock(spec=BookSerializer)
        mock_book_instance = MagicMock(spec=Book)
        mock_book_serializer.is_valid.return_value = True
        mock_book_serializer.save.return_value = mock_book_instance

        self.view.get_serializer = MagicMock(return_value=mock_book_serializer)
        response = self.view.post(_request)
