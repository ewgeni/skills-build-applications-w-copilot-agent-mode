from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Workout, LeaderboardEntry
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardEntrySerializer
from django.db.models import Sum

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardView(generics.ListAPIView):
    serializer_class = LeaderboardEntrySerializer

    def get_queryset(self):
        # Aggregation: Summe der Aktivitätsdauer pro User
        qs = Activity.objects.values('user').annotate(total_duration=Sum('duration')).order_by('-total_duration')
        # Dummy-Objekte für Serialisierung
        entries = []
        for entry in qs:
            user = User.objects.get(id=entry['user'])
            entries.append(LeaderboardEntry(user=user, total_duration=entry['total_duration']))
        return entries

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'workouts': '/workouts/',
        'leaderboard': '/leaderboard/',
    })
