from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.db.models import Count
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        created_games = Game.objects.all()
        ctx = {'created_games': created_games}
        return render(request, 'home.html', ctx)
    

class GameSelectorView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_selector.html'
    context_object_name = 'games'

    

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'create.html'
    success_url = reverse_lazy('main:home_page')
    fields = '__all__'


    def form_valid(self, form):
        game = form.save()

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
    

class GameQuestionCreateListView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_questions_update_selector.html'
    context_object_name = 'games'

class QuestionUpdateListView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'question_updator.html'
    context_object_name = 'game'


class QuestionCreateAndUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'create.html'
    fields = ['question_text', 'question_image', 'answer']

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['is_game'] = True 
        return ctx

    def get_success_url(self) -> str:
        return reverse_lazy('main:question_update_list', args=[self.object.game.id])


class GameUpdateListView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_updator.html'
    context_object_name = 'games'


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = 'create.html'
    success_url = reverse_lazy('main:home_page')
    fields = ('name',)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['message'] = 'You cannot update categories once set as it will cause data inconsistencies. Consider creating a new game'
        return ctx


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('main:home_page')


class GamePlayView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'game_board.html'
    context_object_name = 'game'


class TeamSetView(LoginRequiredMixin, View):
    def get(self, request, game_id):
        ctx = {'game_id': game_id}
        return render(request, 'team_set.html', ctx)

class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'show_question.html'
    context_object_name = 'question'


class ResultsView(LoginRequiredMixin, TemplateView):
    template_name = 'results.html'