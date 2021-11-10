from django.urls import path
from . import views

urlpatterns =[
    path('materials/<int:id>', views.resource, name='resources'),
    path('borrowed/<int:id>', views.borrowed,name='borrowed_materials')
]