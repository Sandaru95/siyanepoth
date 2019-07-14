from django.db import models

class Publisher(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField()

    def __str__(self):
        return self.title

class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo = models.ImageField()

    def __str__(self):
        return self.name

class GreatQuote(models.Model):
    great_quote = models.CharField(max_length=2000)
    narrator = models.CharField(max_length=200)

    def __str__(self):
        return str(self.great_quote + ' : ' + self.narrator)