from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to='gallery/images/')

    def __str__(self):
        return self.title
