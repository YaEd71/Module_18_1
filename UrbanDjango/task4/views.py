from django.shortcuts import render
# Create your views here.

def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    games_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay']
    return render(request, 'fourth_task/games.html', {'games': games_list})

def cart(request):
    return render(request, 'fourth_task/cart.html')
