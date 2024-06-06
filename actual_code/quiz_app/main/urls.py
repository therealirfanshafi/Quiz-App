from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),

    path('game-create', views.GameCreateView.as_view(), name='game_create'),
    path('game-question-create-list', views.GameQuestionCreateListView.as_view(), name='game_question_create_list'),
    path('question-update-list/<int:pk>', views.QuestionUpdateListView.as_view(), name='question_update_list'),
    path('question-create/<int:pk>', views.QuestionCreateAndUpdateView.as_view(), name='question_create_or_update'),

    path('game-update-list', views.GameUpdateListView.as_view(), name='game_update_list'),
    path('game-update/<int:pk>', views.GameUpdateView.as_view(), name='game_update'),
    path('game-delete/<int:pk>', views.GameDeleteView.as_view(), name='game_delete'),
    
    path('game-selection', views.GameSelectorView.as_view(), name='game_selection'),
    path('team-set/<int:game_id>', views.TeamSetView.as_view(), name='team_set'),
    path('game-play/<int:pk>', views.GamePlayView.as_view(), name='game_board'),
    path('question-view/<int:pk>', views.QuestionDetailView.as_view(), name='show_question'),
    path('results', views.ResultsView.as_view(), name='results')
]