from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('user.urls')),
    path('', views.first, name='first'),
    path('dashboard', views.home, name='home')
]