from django.db import models

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.name