from django.contrib import admin
from .models import BodyWeight, Excercise, WorkOut, WorkoutWeight, Workout_data
# Register your models here.


admin.site.register(WorkOut)
admin.site.register(BodyWeight)
admin.site.register(WorkoutWeight)
admin.site.register(Workout_data)
admin.site.register(Excercise)