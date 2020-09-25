from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Solution
import math

# Create your views here.
def loadView(request):
    answer = {
        'solutions': ''
    }
    return render(request, 'quadratic-equations/quadratic-equations.html', answer)

def solve(request):
    #if no value provided for a set default 1
    if(request.POST['a'] == ''):
        a = 1
    else:
        a = int(request.POST['a'])
    if(request.POST['b'] == ''):
        b = 0
    else:
        b = int(request.POST['b'])
    if(request.POST['c'] == ''):
        c = 0
    else:
        c = int(request.POST['c'])

    if(a == 0):
        answer = {
            'a': a,
        }
        return render(request, 'quadratic-equations/quadratic-equations.html', answer)
    dis = (b**2)-(4*a*c)
    if(dis < 0):
        answer = {
            'a': a,
            'b': b,
            'c': c,
            'd': dis,
            'denominator': 2*a
        }
    elif(dis > 0):
        sol1 = (-b - math.sqrt(dis))/(2*a)
        sol2 = (-b + math.sqrt(dis))/(2*a)
        answer = {
            'sol1': sol1,
            'sol2': sol2,
            'a': a,
            'b': b,
            'c': c,
            'd': dis,
            'denominator': 2*a
        }
    else:
        sol1 = (-b - math.sqrt(dis))/(2*a)
        answer = {
            'sol1': sol1,
            'a': a,
            'b': b,
            'c': c,
            'd': math.sqrt(dis),
            'denominator': 2*a
        }
    return render(request, 'quadratic-equations/quadratic-equations.html', answer)
