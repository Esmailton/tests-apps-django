from django.db import models
from apps.core.models import Base


class Book(Base, models.Model):
    title = models.CharField("Book Title", max_length=20)
    description = models.CharField(
        "Book Description", max_length=20, blank=True, null=True)
    pages = models.PositiveIntegerField("Book Number")
    author = models.CharField("Book Autor", max_length=20)
    status = models.CharField("Book Status", choices=(
                              ("1", "available"), ("2", "busy")), max_length=15)

    def __str__(self):
        return self.title
