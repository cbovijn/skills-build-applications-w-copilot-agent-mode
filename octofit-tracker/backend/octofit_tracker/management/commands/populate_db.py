from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [User(**user_data) for user_data in test_users]
        User.objects.bulk_create(users)

        # Create teams
        teams = [Team(**team_data) for team_data in test_teams]
        Team.objects.bulk_create(teams)

        # Assign users to teams
        for team in Team.objects.all():
            team.members.set(User.objects.all())

        # Create activities
        activities = [
            Activity(user=User.objects.get(username=test_users[i]['username']), **activity_data)
            for i, activity_data in enumerate(test_activities)
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=Team.objects.first(), **entry_data)
            for entry_data in test_leaderboard
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [Workout(**workout_data) for workout_data in test_workouts]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
