from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('game-selection', views.GameSelectorView.as_view(), name='game_selection'),
    path('game-create', views.GameCreateView.as_view(), name='game_create'),
    path('question-create', views.QuestionCreateView.as_view(), name='question_create'),
    path('game-update-list', views.GameUpdateListView.as_view(), name='game_update_list'),
    path('game-update/<int:pk>', views.GameUpdateView.as_view(), name='game_update'),
    path('game-delete/<int:pk>', views.GameDeleteView.as_view(), name='game_delete'),
    path('question-update-list/<int:pk>', views.QuestionUpdateListView.as_view(), name='question_update_list'),
    path('question-update/<int:pk>', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question-delete/<int:pk>', views.QuestionDeleteView.as_view(), name='question_delete')
]