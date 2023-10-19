from django.db import models


class Person(models.Model):
    first = models.TextField()
    last = models.TextField()


    def __str__(self):
        return f"{self.id}. {self.first} {self.last}"
    