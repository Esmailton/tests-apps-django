from django.forms import ValidationError
from django.test import TestCase
from apps.library.test.unit.factories import BookFactory, PersonFactory, RentalFactory
from parameterized import parameterized
from apps.library.models import Person, Rental, Book


class TestBookModel(TestCase):

    def setUp(self):
        self.book = BookFactory.build()

    def test_book_representation_test(self):
        book = self.book
        self.assertIsInstance(book, Book)
        self.assertEqual(str(book), book.title)

    def test_book_requirement_field_exceptions(self):
        with self.assertRaises(ValidationError):
            book_exeptions = BookFactory.build(
                title=None, pages=None, author=None, status=None)
            book_exeptions.clean_fields()

    @parameterized.expand(
        [
            ("title", 20),
            ("description", 200),
            ("status", 2),
        ]
    )
    def test_fields_max_length_exceptions(self, field, max_length):
        book = self.book
        setattr(book, field, "x" * (max_length + 1))
        with self.assertRaises(ValidationError):
            book.clean_fields()


class TestPerson(TestCase):
    def setUp(self):
        self.person = PersonFactory.build()

    def test_person_str_representation(self):
        person = self.person
        self.assertIsInstance(person, Person)
        self.assertEqual(str(person), person.full_name)

    def test_person_requirement_field_exceptions(self):
        with self.assertRaises(ValidationError):
            person_null_fields = PersonFactory.build(
                full_name=None, document=None, email=None, phone=None)
            person_null_fields.clean_fields()

    @parameterized.expand(
        [
            ("full_name", 50),
            ("document", 11),
            ("phone", 15),
        ]
    )
    def test_fields_max_length_exceptions(self, field, max_length):
        person = self.person
        setattr(person, field, "x" * (max_length + 1))
        with self.assertRaises(ValidationError):
            person.clean_fields()


class TestRental(TestCase):

    def setUp(self):
        self.rental = RentalFactory.build()

    def test_rental_instance(self):
        rental = self.rental
        self.assertIsInstance(rental, Rental)

    def test_rental_requirement_field_exceptions(self):
        with self.assertRaises(ValidationError):
            rental_null_fields = RentalFactory.build(
                book=None, person=None)
            rental_null_fields.clean_fields()
