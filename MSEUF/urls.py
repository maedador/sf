
from django.urls import path
from . import views 

urlpatterns = [
    path('Mission', views.Mission, name='mission'),
    path('Vision', views.Vision, name='vision'),
    path('Goal', views.Goal, name='goal'),

]
