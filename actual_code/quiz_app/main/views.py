from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


#main page from which all other menus are to be created
class Home(LoginRequiredMixin, View):
    def get(self, request):
        created_games = Game.objects.all()
        ctx = {'created_games': created_games}
        return render(request, 'home.html', ctx)
    

# a view in which the games are created
class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'create.html'
    success_url = reverse_lazy('main:home_page')
    fields = '__all__'


    def form_valid(self, form):
        game = form.save()

        # after creating a game, default questions are created so that there is no unfinished game
        for i in range(game.number_of_questions_per_category):
            Question.objects.create(game=game, points = (i + 1)*100, category = game.category_1)

        for i in range(game.number_of_questions_per_category):
             Question.objects.create(game=game, points = (i + 1)*100, category = game.category_2)

        if game.category_3:
            for i in range(game.number_of_questions_per_category):
             Question.objects.create(game=game, points = (i + 1)*100, category = game.category_3)

        if game.category_4:
            for i in range(game.number_of_questions_per_category):
             Question.objects.create(game=game, points = (i + 1)*100, category = game.category_4)

        return super().form_valid(form)
    

# a view in which a game can be selected to create the questions for it
class GameQuestionCreateListView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_questions_update_selector.html'
    context_object_name = 'games'


# a board of a particular game in which the questions can be updated. Since the questions are automatically created when a game is created, the questions can only be updated. This prevents incorrect number of questions being created and ensures that valid categories and points are input without duplicates
class QuestionUpdateListView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'question_updator.html'
    context_object_name = 'game'


# the view to update the questions of a game
class QuestionCreateAndUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'create.html'
    fields = ['question_text', 'question_image', 'answer']

    # this extra data is added to the context so that the template can differentiate between the game create/update view and the question update view
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['is_game'] = True 
        return ctx

    # this allows the user to be redirected to the game update board after creating a question rather than to the home page which would be annoying to use
    def get_success_url(self):
        return reverse_lazy('main:question_update_list', args=[self.object.game.id])


# a view of a list of games to allow the games to be updated
class GameUpdateListView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_updator.html'
    context_object_name = 'games'


# view to update the games
class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = 'create.html'
    success_url = reverse_lazy('main:home_page')
    fields = ('name',)

    # adds extra data to the context to provide reasoning to the users as to why the categories of a game cannot be updated once set
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['message'] = 'You cannot update categories once set as it will cause data inconsistencies. Consider creating a new game'
        return ctx


# a view to delete the game
class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('main:home_page')


# a view in which a game can be selected to be played
class GameSelectorView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_selector.html'
    context_object_name = 'games'


# a client side view to set the teams in temporary browser memory
class TeamSetView(LoginRequiredMixin, View):
    def get(self, request, game_id):
        ctx = {'game_id': game_id}
        return render(request, 'team_set.html', ctx)


# the view of the game board in order to play the game 
class GamePlayView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'game_board.html'
    context_object_name = 'game'

    # polymorphises this method to add additional data for the total number of questions in the game, so that this data can be used client side
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        num_categories = 2
        game = self.get_object()

        if game.category_3:
            num_categories += 1
        
        if game.category_4:
            num_categories +=1

        ctx['total_questions'] = num_categories * game.number_of_questions_per_category

        return ctx

# shows each question in a game with a lot of client side scripting involved
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'show_question.html'
    context_object_name = 'question'


# a client rendered view which shows the results of a game after is over
class ResultsView(LoginRequiredMixin, TemplateView):
    template_name = 'results.html'