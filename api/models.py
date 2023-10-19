from django.db import models


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()


    def __str__(self):
        return f"{self.id}. {self.name}"
    