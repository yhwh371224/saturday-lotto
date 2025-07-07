from django.shortcuts import render
from django.http import HttpResponse
from random import sample

def lotto(request):
    if request.method == 'POST':
        try:
            n = int(request.POST.get('num_games'))
        except (ValueError, TypeError):
            return render(request, 'index.html', {'error': "Please enter a valid number."})
        
        lotto_numbers = list(range(1, 46))
        games = []
        for _ in range(n):
            winner_numbers = sample(lotto_numbers, 6)
            winner_numbers.sort()
            games.append(winner_numbers)
        
        return render(request, 'index.html', {'games': games})
    else:
        return render(request, 'index.html')

