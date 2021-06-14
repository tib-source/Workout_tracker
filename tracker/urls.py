from django.urls import path
from .views import dashboard_view, homeview

urlpatterns=[
    path('', homeview, name='home'),
    path('dashboard/', dashboard_view, name='dashboard')  ### insert view here
]