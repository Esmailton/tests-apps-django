from django.urls import path
from apps.library.api.views.book import BookListCreateView

app_name = "library"

urlpatterns = [
    path("v1/library/", BookListCreateView.as_view(), name="library-api"),
]
