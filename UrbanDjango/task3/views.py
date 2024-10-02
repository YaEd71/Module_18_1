from django.shortcuts import render
# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    games_list = {
        'Atomic Heart': '2999 руб.',
        'Cyberpunk 2077': '3999 руб.',
        'PayDay': '1999 руб.'
    }
    return render(request, 'third_task/games.html', {'games': games_list})

def cart(request):
    return render(request, 'third_task/cart.html')
from django.shortcuts import render


