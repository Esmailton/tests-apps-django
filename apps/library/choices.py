from django.db.models import IntegerChoices


class BookStatusChoice(IntegerChoices):
    AVAILABLE = 1
    BUSY = 2
