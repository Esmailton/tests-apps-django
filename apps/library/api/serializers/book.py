from rest_framework import serializers
from apps.library.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["title", "description", "pages", "author",
                  "status", "created_at", "updated_at", "id"]
        read_only_fields = ['updated_at', "created_at", "id", "status"]
