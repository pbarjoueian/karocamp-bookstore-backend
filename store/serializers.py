from rest_framework import serializers

from .models import Author, Book, Publication


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "website",
            "phone_number",
            "birthdate",
            "language",
            "is_translator",
            "created_at",
            "updated_at",
            "created_by",
        )
        read_only_fields = ("id", "created_at", "updated_at", "created_by")


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = (
            "id",
            "name",
            "phone_number",
            "address",
            "created_at",
            "updated_at",
            "created_by",
        )
        read_only_fields = ("id", "created_at", "updated_at", "created_by")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at", "created_by")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = AuthorSerializer(instance.author).data
        representation["publication"] = PublicationSerializer(instance.publication).data
        return representation
