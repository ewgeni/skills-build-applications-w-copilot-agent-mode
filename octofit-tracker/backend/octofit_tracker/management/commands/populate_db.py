from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Lösche alle Daten
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Activities
        octo_models.Activity.objects.create(user=ironman, type='Run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=spiderman, type='Swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=batman, type='Bike', duration=60, distance=20)
        octo_models.Activity.objects.create(user=superman, type='Run', duration=50, distance=10)

        # Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Leaderboard
        octo_models.Leaderboard.objects.create(team=marvel, points=100)
        octo_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db erfolgreich mit Testdaten befüllt.'))
