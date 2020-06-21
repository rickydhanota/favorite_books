from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title'] = "A title MUST be provided!"
        if len(postData['description'])<5:
            errors['description'] = "Description MUST be atleast 5 characters long"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey('login.User', related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField('login.User', related_name='liked_books')
    objects = BookManager()