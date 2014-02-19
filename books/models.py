from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=20)
    author_firstname = models.CharField(max_length=20)
    author_lastname = models.CharField(max_length=20)
    in_stock = models.BooleanField(default=True)
    # title_author = (title, author)

    def __unicode__(self):
        return self.title
        return self.author_firstname
        return self.author_lastname
