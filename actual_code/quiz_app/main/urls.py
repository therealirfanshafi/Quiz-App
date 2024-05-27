from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('game-selection', views.GameSelectorView.as_view(), name='game_selection'),
    path('game-create', views.GameCreateView.as_view(), name='game_create'),
    path('question-create', views.QuestioNCreateView.as_view(), name='question_create')
]