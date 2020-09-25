from django.urls import path
from . import views
urlpatterns = [
    path('loadView/', views.loadView, name='loadView'),
    path('solve/', views.solve, name='solve'),
]