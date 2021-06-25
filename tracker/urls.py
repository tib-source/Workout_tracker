from django.urls import path
from .views import dashboard_view, homeview, weight_view

urlpatterns=[
    path('', dashboard_view, name='dashboard'),  ### insert view here
    path('weight/', weight_view, name='weight'),
]