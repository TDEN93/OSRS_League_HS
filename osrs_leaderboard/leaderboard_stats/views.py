from django.shortcuts import render
from django.http import HttpResponse
from .models import league_hiscores

stats = [
    {
        'rank': 1,
        'name': 'Tetro',
        'level': 200,
        'exp': 200000,
    }
]

def home(request):
    context = {
        'stats': league_hiscores.objects.all()
    }
    return render(request, 'leaderboard_stats/home.html', context)
