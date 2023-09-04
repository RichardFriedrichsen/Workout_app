from django.db import models

# Exercises to select from
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Model for workouts
class Workout(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return f"{self.date} {self.title}"

# Model for exercises within workouts
class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.workout.title} - {self.exercise.name}"

