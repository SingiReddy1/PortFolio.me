from django.db import models

# Create your models here.

class AddMsg(models.Model):
    name = models.CharField(max_length=50)
    msg = models.TextField()
    email = models.CharField(max_length=60)

    def __str__(self):
        return self.name
        