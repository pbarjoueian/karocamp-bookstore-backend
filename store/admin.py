from django.contrib import admin

from store.models import Author, Book, Publication

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publication)
