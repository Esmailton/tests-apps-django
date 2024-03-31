import factory
from apps.library.models import Book, Person, Rental
from faker import Faker
from datetime import timedelta

fake = Faker("pt_BR")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = factory.LazyAttribute(lambda _: fake.word())
    description = factory.LazyAttribute(
        lambda _: fake.sentences())
    pages = factory.LazyAttribute(
        lambda _: fake.random_int(min=50, max=1000))
    author = factory.LazyAttribute(lambda _: fake.name())
    created_at = factory.LazyAttribute(
        lambda _: fake.date_time_between(start_date="-1y", end_date="now"))
    updated_at = factory.LazyAttribute(
        lambda _: fake.date_time_between(start_date="-1y", end_date="now"))


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
    full_name = factory.LazyAttribute(lambda _: fake.name())
    document = factory.LazyAttribute(lambda _: fake.cpf())
    email = factory.LazyAttribute(lambda _: fake.email())
    phone = factory.LazyAttribute(lambda _: fake.phone_number())


class RentalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rental

    book = factory.SubFactory(BookFactory)
    person = factory.SubFactory(PersonFactory)
    days = factory.LazyAttribute(lambda _: fake.random_int(10, 100))
    start_date = factory.LazyAttribute(
        lambda _: fake.date_between('-30d', 'today'))
    end_date = factory.LazyAttribute(
        lambda obj: obj.start_date + timedelta(days=obj.days))
