from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import BoardGame
from .forms import BoardGameForm


def receive_collection_list(request):
    board_games = BoardGame.objects.all()
    return render(request, 'collection/collection_list.html', {'board_games': board_games})


def show_board_game_detail(request, pk):
    board_game = get_object_or_404(BoardGame, pk=pk)
    return render(request, 'collection/board_game_detail.html', {'board_game': board_game})


def add_board_game(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            board_game = form.save(commit=False)
            board_game.owner = request.user
            board_game.published_date = timezone.now()
            board_game.save()
            return redirect('board_game_detail', pk=board_game.pk)
    else:
        form = BoardGameForm()
    return render(request, 'collection/edit_board_game.html', {'form': form})


def edit_board_game(request, pk):
    board_game = get_object_or_404(BoardGame, pk=pk)
    if request.method == "POST":
        form = BoardGameForm(request.POST, instance=board_game)
        if form.is_valid():
            board_game = form.save(commit=False)
            board_game.author = request.user
            board_game.published_date = timezone.now()
            board_game.save()
            return redirect('board_game_detail', pk=board_game.pk)
    else:
        form = BoardGameForm(instance=board_game)
    return render(request, 'collection/edit_board_game.html', {'form': form})
