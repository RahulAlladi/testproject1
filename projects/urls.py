from django.urls import path
from . import views

urlpatterns=[
        path('',views.projects,name="projects"),
        path('project/<str:pk>',views.project2,name="project"),
]