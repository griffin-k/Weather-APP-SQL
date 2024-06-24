from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .weatherInfo import check_weather
from .models import UserLogin, History, JoinThis
from django.db.models import Q
from django.urls import reverse
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def home(request):
    # return HttpResponse("This is the home Page")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dateTime = datetime.now()
        userLogin = UserLogin(name = name, email = email, dateTime = dateTime)
        userLogin.save()
    
    return render(request, 'home.html')


def search(request):
    if request.method == 'POST':
        search = request.POST.get('city')
        weather = check_weather(search)

        if weather == 'Error':
            print(weather)
            return render(request, 'home.html')


        last_user_login = UserLogin.objects.last()
        print("**************")
        print(last_user_login.name)
        print(last_user_login.email)
        print("**************")

        city = weather['name']
        dateTime = weather['datetime']

        if last_user_login:
            name = last_user_login.name
            email = last_user_login.email
        else:
            name = "-"
            email = "-"
        
        history_data = History(
            city=city,
            dateTime=dateTime,
        )
        history_data.save()
        
        join_table = JoinThis(
            name = name,
            userEmail = email,
            cityName = city,
            dateTime = dateTime,
        )
        try:
            join_table.save()
        except:
            pass

        return render(request, 'search.html', weather)

    return render(request, 'search.html') 


def userLogin(request):
    return render(request, 'login.html')


def showTables(request):
    items = UserLogin.objects.all().values()
    history = History.objects.all().values()
    join = JoinThis.objects.all().values()
    print(history)
    context = {
        'items': items,
        'history': history,
        'join' : join,
    }
    return render(request, 'showTables.html', context)


def deleteRow(request, id):
    try:
        item = UserLogin.objects.get(id=id)
        try:
            item.delete()
        except:
            pass
    except UserLogin.DoesNotExist:
        pass
    return redirect('showTables')


def deleteHistoryRow(request, id):
    try:
        item = History.objects.get(id=id)
        try:
            item.delete()
        except:
            pass
    except:
        pass
    return redirect('showTables')


def deleteJoin(request, id):
    try:
        item = JoinThis.objects.get(id=id)
        try:
            item.delete()
        except:
            pass
    except:
        pass
    return redirect('showTables')
