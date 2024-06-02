from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Count
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

# Create your views here.
class Home(LoginRequiredMixin, View):
    def get(self, request):
        created_games = Game.objects.all()
        completed_games = Game.objects.annotate(num_qs=Count('question')).filter(num_qs=20)
        ctx = {'created_games': created_games, 'completed_games':completed_games}
        return render(request, 'home.html', ctx)
    

class GameSelectorView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'game_selector.html'
    context_object_name = 'games'

    def get_queryset(self) -> QuerySet[Any]:
        games = super().get_queryset()
        games = games.annotate(num_qs=Count('question')).filter(num_qs=20)
        if games:
            return games
        return redirect(reverse_lazy('main:home_page'))
    

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'create.html'
    success_url = reverse_lazy('main:home_page')
    fields = '__all__'


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('main:home_page')


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


class QuestionUpdateListView(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'question_updator.html'
    context_object_name = 'game'


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('main:game_update_list')


class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('main:game_update_list')


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