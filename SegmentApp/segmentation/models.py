from django.db import models


class NewImage(models.Model):
    image = models.ImageField(upload_to='images/input/')
