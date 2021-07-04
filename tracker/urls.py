from django.urls import path
from .views import WorkoutView, dashboard_view, homeview, log_workout_view, weight_view

urlpatterns=[
    path('', dashboard_view, name='dashboard'),  ### insert view here
    path('weight/', weight_view, name='weight'),
    path('workouts/', WorkoutView.as_view(), name='workout'),
    path('new-workout/', log_workout_view, name='new-workout'),
]