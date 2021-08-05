from django.db import models


class Goods(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title
