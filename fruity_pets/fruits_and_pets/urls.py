from django.urls import path
from .views import FruitsView, FruitDetailView, PetsView, PetDetailView

urlpatterns = [
    path('fruits/', FruitsView.as_view(), name='fruits_index_and_create'),
    path('fruits/<int:pk>/', FruitDetailView.as_view(), name='fruits_show_update_and_delete'),
    path('pets/', PetsView.as_view(), name='pets_index_and_create'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pets_show_update_and_delete')
]