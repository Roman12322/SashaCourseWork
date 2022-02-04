from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User, Calculations
from django.db.utils import IntegrityError
from django.contrib import messages
import numpy as np

def calcs(request):
    return render(request, 'calcs.html')

def data(request):
    return render(request, 'data.html')

def signup(request):
    return render(request, 'main.html')

def Registration(request):
    try:
        if request.method == "POST":
            user = User()
            Login = request.POST.get("userName")
            Pass = request.POST.get("pwd")
            if len(Login) > 4 and len(Pass) > 4:
                user.Login = request.POST.get("userName")
                user.Password = request.POST.get("pwd")
                user.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/calcs")
            else:
                data = {
                    'userName': Login,
                    'pwd': Pass,
                }
                messages.error(request, 'Login and password must be over 4 letters')
                return render(request, "main.html", data)
    except IntegrityError:
        data = {
            'userName': Login,
            'pwd': Pass,
        }
        messages.error(request, "User's login is busy. Try another please")
        return render(request, "main.html", data)

def Calculate(request):
    if request.method == "POST":
        username = request.POST.get("userName")
        password = request.POST.get("pwd")
        seq1 = request.POST.get("sequence1")
        seq2 = request.POST.get("sequence2")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                result = function(seq1, seq2)
                data = {
                    'userName': username,
                    'pwd': password,
                    'sequence1': seq1,
                    'sequence2': seq2,
                    'result': result
                }
                tmp = Calculations.objects.create(sqn1=seq1, sqn2=seq2, result=result, userId=checkUserLogin.id)
                messages.success(request, "Вычисления проведены успешно и добавлены в базу данных")
                return render(request, "calcs.html", data)
        except User.DoesNotExist:
            messages.error(request, "Неверный логин или пароль")
            data = {
                'userName': username,
                'pwd': password,
            }
            return render(request, "calcs.html", data)
    return HttpResponseRedirect("http://127.0.0.1:8000/result")

def getData(request):
    if request.method == "POST":
        username = request.POST.get("userName")
        password = request.POST.get("pwd")
        try:
            data = {
                'userName': username,
                'pwd': password,
            }
            checkUserData = User.objects.get(Login=username, Password=password)
            results = Calculations.objects.filter(userId=checkUserData.id)
            return render(request, "data.html", {'results': results})
        except User.DoesNotExist:
            messages.error(request, "Неверный логин или пароль")
            data = {
                'userName': username,
                'pwd': password,
            }
            return render(request, "data.html", data)

    return HttpResponseRedirect("http://127.0.0.1:8000/Results")

def function(seq1, seq2):
    if seq1 is None or seq2 is None:
        message = 'Введены неверные данные'
        return message
    else:
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in range(size_x):
            matrix [x, 0] = x
        for y in range(size_y):
            matrix [0, y] = y

        for x in range(1, size_x):
            for y in range(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
        return (matrix[size_x - 1, size_y - 1])
