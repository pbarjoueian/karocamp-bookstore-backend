from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from account.models import UserData


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_by = models.ForeignKey(UserData, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    first_name = models.CharField(max_length=128, null=False, blank=True)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=False, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=128, null=False, blank=True)
    is_translator = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Publication(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=128, null=False, blank=False)
    year = models.IntegerField(
        null=False,
        default=2000,
        validators=[MaxValueValidator(4000), MinValueValidator(500)],
    )
    pages_number = models.PositiveIntegerField(null=False)
    description = models.TextField(null=True, blank=True)
    isbn = models.IntegerField(null=False, blank=True)
    amount = models.IntegerField(null=False, default=1)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    translator = (
        models.ForeignKey(
            Author,
            on_delete=models.CASCADE,
            related_name="book_translator",
            null=True,
            blank=True,
        ),
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="book_author"
    )

    def __str__(self):
        return f"{self.title} | {self.author} | {self.publication} | {self.amount}"
