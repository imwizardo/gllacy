from django.db import models

class Filler(models.Model):
    FILLER_CHOICES = [
        ('chocolate', 'Шоколадные'),
        ('sugar_sprinkles', 'Сахарные присыпки'),
        ('fruits', 'Фрукты'),
        ('syrups', 'Сиропы'),
        ('jams', 'Джемы'),
    ]
    name = models.CharField(max_length=50, unique=True, choices=FILLER_CHOICES)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="products")
    is_hit = models.BooleanField(default=False)
    fat = models.IntegerField(default=0)
    fillers = models.ManyToManyField(Filler, related_name="products", blank=True, null=True)

    def __str__(self):
        return self.name
