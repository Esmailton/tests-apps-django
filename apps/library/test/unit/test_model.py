from django.test import TestCase
from apps.library.test.unit.factories import BookFactory


class TestBookModel(TestCase):

    def setUp(self):
        self.book = BookFactory.build()

    def test_book_representation_test(self):
        book = self.book
        self.assertEqual(str(book), book.title)

    def test_book_requirement_field_exceptions(self):

        with self.assertRaises(TypeError) as context:
            book = BookFactory.build(
                title=100, description=None, author=None, pages=None)
            breakpoint()
