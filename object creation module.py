
from tracker.models import *

stronglift = WorkOut.objects.first()
bench = Excercise.objects.create(
    name='Bench Press'
)
squat = Excercise.objects.create(
    name='Squat'
)
barbell_row = Excercise.objects.create(
    name='Barbell Row'
)
overhead_press = Excercise.objects.create(
    name='Overhead Press'
)
deadlift = Excercise.objects.create(
    name='Deadlift'
)

stronglift.excercise.add(
    bench,
    squat,
    barbell_row,
    overhead_press,
    deadlift,
)