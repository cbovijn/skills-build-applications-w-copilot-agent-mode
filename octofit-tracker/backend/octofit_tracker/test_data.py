from datetime import datetime, timedelta

test_users = [
    {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
    {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]

test_teams = [
    {"name": "Blue Team"},
    {"name": "Gold Team"},
]

test_activities = [
    {"activity_type": "Cycling", "duration": 60, "calories_burned": 500, "date": datetime(2025, 4, 8)},
    {"activity_type": "Crossfit", "duration": 120, "calories_burned": 800, "date": datetime(2025, 4, 7)},
    {"activity_type": "Running", "duration": 90, "calories_burned": 600, "date": datetime(2025, 4, 6)},
    {"activity_type": "Strength", "duration": 30, "calories_burned": 200, "date": datetime(2025, 4, 5)},
    {"activity_type": "Swimming", "duration": 75, "calories_burned": 700, "date": datetime(2025, 4, 4)},
]

test_leaderboard = [
    {"points": 100},
    {"points": 90},
    {"points": 95},
    {"points": 85},
    {"points": 80},
]

test_workouts = [
    {"name": "Cycling Training", "description": "Training for a road cycling event", "difficulty": "Intermediate"},
    {"name": "Crossfit", "description": "Training for a crossfit competition", "difficulty": "Advanced"},
    {"name": "Running Training", "description": "Training for a marathon", "difficulty": "Intermediate"},
    {"name": "Strength Training", "description": "Training for strength", "difficulty": "Beginner"},
    {"name": "Swimming Training", "description": "Training for a swimming competition", "difficulty": "Intermediate"},
]
