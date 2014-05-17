from django.db import models

from home.models import Event

from author.models import Author

class Article(models.Model):
    event = models.ForeignKey(Event)
    author = models.ForeignKey(Author)
    is_beta = models.BooleanField()
    text = models.TextField()

    def get_absolute_url(self):
        return '/article/' + str(self.id)
