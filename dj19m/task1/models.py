from django.db import models
# Create your models here.


class Buyer(models.Model):

    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):

    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
