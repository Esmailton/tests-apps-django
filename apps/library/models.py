from django.db import models
from apps.core.models import Base
from apps.library.choices import BookStatusChoice


class Book(Base, models.Model):
    title = models.CharField("Book Title", max_length=20)
    description = models.TextField(
        "Book Description", blank=True, null=True)
    pages = models.PositiveIntegerField("Book Number")
    author = models.CharField("Book Author", max_length=20)
    status = models.PositiveSmallIntegerField(
        "Book Status", choices=BookStatusChoice.choices, default=BookStatusChoice.AVAILABLE)

    def __str__(self):
        return self.title


class Person(Base, models.Model):
    full_name = models.CharField("Full Name", max_length=50)
    document = models.CharField("Full Name", max_length=11, unique=True)
    email = models.EmailField("E-mail", unique=True)
    phone = models.CharField("Phone", max_length=15, unique=True)

    def __str__(self):
        return self.full_name


class Rental(Base, models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='rental')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name='rental')
    days = models.PositiveIntegerField("Days")
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
