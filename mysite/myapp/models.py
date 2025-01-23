from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=55)
    book_author = models.TextField()
    release_date = models.TextField()

    def __str__(self):
        return (f'Title: {self.title}, Author: {self.book_author}, Release year: {self.release_date}')



