import factory
from apps.library.models import Book
from faker import Faker
import random


fake = Faker()


class BookFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Book
    title = factory.LazyAttribute(lambda _: "Book Title %s" % fake.word())
    description = factory.LazyAttribute(
        lambda _: " Description: %s" % fake.sentences())
    pages = factory.LazyAttribute(
        lambda _: fake.random_int(min=50, max=1000))
    author = factory.LazyAttribute(lambda _: fake.name())
    status = random.choice(["available", "busy"])
