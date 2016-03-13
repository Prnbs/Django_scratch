from django.db import models


class Tags(models.Model):
    tags = models.TextField()

    def __str__(self):
        return self.tags


class URL(models.Model):
    url = models.TextField()
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.url


class User(models.Model):
    email = models.EmailField()
    url = models.ManyToManyField(URL)

    def __str__(self):
        return self.email


class URLMetaData(models.Model):
    url = models.TextField()
    blurb = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.url