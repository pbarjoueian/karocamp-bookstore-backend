from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, PublicationViewSet

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"author", AuthorViewSet, basename="author")
router.register(r"publication", PublicationViewSet, basename="publication")
router.register(r"book", BookViewSet, basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
