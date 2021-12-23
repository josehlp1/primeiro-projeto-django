from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} que tem {}</h1>'.format(nome, idade))

def soma(request, num1, num2):
    return HttpResponse('<h1>A soma dos dois valores enviados é {}</h1>'.format(num1 + num2))

def subtracao(request, num1, num2):
    return HttpResponse('<h1>A subtração dos dois valores enviados é {}</h1>'.format(num1 - num2))

def divicao(request, num1, num2):
    return HttpResponse('<h1>A subtração dos dois valores enviados é {}</h1>'.format(num1 / num2))

def multiplicacao(request, num1, num2):
    return HttpResponse('<h1>A subtração dos dois valores enviados é {}</h1>'.format(num1 * num2))
