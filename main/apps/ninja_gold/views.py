from django.shortcuts import render, redirect
import random
from time import gmtime, strftime


coin_values = {
    'farm': [10, 20],
    'cave': [5, 10],
    'house': [2, 5],
    'casino': [0, 50]
}

def index(request):
  if 'total' not in request.session:
    request.session['total'] = 0
    request.session['log'] = []
  return render(request, 'index.html')

def process_money(request):
  values = coin_values[request.POST['place']]
  value = random.randint(values[0], values[1])
  if request.POST['place'] == 'casino' and random.randint(0,1) == 0:
    value *= -1
  timestamp = strftime("%Y-%m-%d %H:%M %p", gmtime())
  request.session['total'] += value
  new_log = {
      'value': value,
      'time': timestamp,
      'place': request.POST['place']
  }
  request.session['log'].append(new_log)
  return redirect('/')

def reset(request):
  del request.session['total']
  return redirect('/')
