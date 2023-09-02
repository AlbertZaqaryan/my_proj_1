from django.shortcuts import render
# Create your views here.

def hello(request):
    return render(request, 'home.html')

def calculator(request):
    res = 0
    if request.method == "POST":
        number1 = request.POST.get("number1")
        char = request.POST.get("char")
        number2 = request.POST.get("number2")
        if char == '+':
            res = int(number1) + int(number2)
        elif char == '-':
            res = int(number1) - int(number2)
        elif char == '*':
            res = int(number1) * int(number2)
        elif char == '/':
            try:
                res = int(number1) / int(number2)
            except ZeroDivisionError:
                res = 'ZeroError'
    return render(request, 'calculator.html', context={'result':res})