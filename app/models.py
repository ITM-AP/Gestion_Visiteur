from django.db import models

# Create your models here.


class Rdv(models.Model):
    dateTime = models.DateTimeField()
    entreprise = models.CharField(max_length=50)
    nombreVisiteur = models.IntegerField()

    def __str__(self):
        return self.entreprise
