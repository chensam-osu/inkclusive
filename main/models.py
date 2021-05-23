from django.db import models

# Create your models here.
class Words(models.Model):

    word = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length= 150,blank=True, null=True)

    def __str__(self):

        return self.word