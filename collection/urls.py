from django.urls import path
from . import views

urlpatterns = [
    path('', views.receive_collection_list, name='collection_list'),
    path('board_game/new/', views.add_board_game, name='new_board_game'),
    path('board_game/<int:pk>/', views.show_board_game_detail, name='board_game_detail'),
    path('board_game/<int:pk>/edit/', views.edit_board_game, name='edit_board_game'),
]
