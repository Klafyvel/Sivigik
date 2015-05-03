from django.db import models
from author.models import Author

class Poll(models.Model):
    question = models.CharField(max_length=200)
    # author = models.ForeignKey(Author)