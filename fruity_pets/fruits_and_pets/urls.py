from django.urls import path
from .views.fruit_views import FruitsView, FruitDetailView 
from .views.pet_views import PetsView, PetDetailView
from .views.toy_views import ToysView, ToyDetailView
from .views.owner_views import OwnersView, OwnerDetailView

urlpatterns = [
    path('fruits/', FruitsView.as_view(), name='fruits_index_and_create'),
    path('fruits/<int:pk>/', FruitDetailView.as_view(), name='fruits_show_update_and_delete'),
    path('pets/', PetsView.as_view(), name='pets_index_and_create'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pets_show_update_and_delete'),
    path('toys/', ToysView.as_view(), name='toys_index_and_create'),
    path('toys/<int:pk>/', ToyDetailView.as_view(), name='toys_show_update_and_delete'),
    path('owners/', OwnersView.as_view(), name='owners_index_and_create'),
    path('owners/<int:pk>/', OwnerDetailView.as_view(), name='owners_show_update_and_delete')
]