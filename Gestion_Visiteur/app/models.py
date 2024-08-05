from django.db import models

# Create your models here.

class Rdv(models.Model):
    date = models.DateField()
    time = models.TimeField()
    entreprise = models.CharField(max_length=50)

    def __str__(self):
        return self.entreprise