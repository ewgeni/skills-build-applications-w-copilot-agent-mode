from djongo import models
from django.contrib.auth.models import AbstractUser

# Benutzerprofil
class User(AbstractUser):
    # Zusätzliche Felder können hier ergänzt werden
    pass

# Team
class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Aktivität
class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Dauer in Minuten')
    date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')

# Workout
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts', blank=True)

# Leaderboard (Aggregation, kein klassisches Modell, aber für API-Serialisierung)
# Kann als Dummy-Modell für Serialisierung genutzt werden
class LeaderboardEntry(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    total_duration = models.PositiveIntegerField()

    class Meta:
        managed = False
        verbose_name = 'Leaderboard Entry'
        verbose_name_plural = 'Leaderboard Entries'
