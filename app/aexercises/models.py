from django.db import models

# Create your models here.

class exercise(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class set(models.Model):
    weight = models.FloatField()
    reps = models.IntegerField()

    class Meta:
        abstract: True
    
class  workout(models.Model):
    name = models.ForeignKey(exercise, on_delete=models.CASCADE)
    sets = models.ManyToManyField(set)
  