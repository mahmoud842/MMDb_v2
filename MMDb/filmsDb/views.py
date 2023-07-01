from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Film, PersonList
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def index(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request, 'index.html', {
        'list': PersonList.objects.filter(user_name=request.user.username)
    })

def filmsList(request):
    films = Film.objects.all()
    return render(request, 'filmsList.html' ,{
            'title':'Films List',
            'styleFile':'',
            'films':films
        })

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "login.html", {
                "message": "Invalid Credentials"
            })


    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return render(request, 'login.html', {
        'message': 'logged out'
    })

def signup(request):
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if not user:
            user = User.objects.create_user(username=request.POST['username'],
                                            password=request.POST["password"],
                                            first_name=request.POST['first_name'])
            user.save()
            login(request,user)
        
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'signup.html')

def addWatchList(request):
    
    if request.method == "POST":
        return render(request, 'addWatchList.html',{
            'films': Film.objects.filter(name__contains=request.POST['search'])
        })

    return render(request, 'addWatchList.html')

def addToList(request, id):

    p = PersonList(user_name=request.user.username, film=Film.objects.get(pk=id))
    p.save()
    return render(request, 'index.html', {
        'list': PersonList.objects.filter(user_name=request.user.username)
    })


# this code snippit extracts data from csv file and save it into Db
# from filmsDb.models import Film
# import csv
# with open('films.csv', newline='') as filmscsv:
#      films_dict = csv.DictReader(filmscsv)
#      for row in films_dict:
#              f = Film(name=row['name'],language=row['language'],rate=row['rating'],type=row['type'])
#              f.save()

# from filmsDb.models import Film
# for i in range(31,60):
#     f = Film.objects.get(pk=i)
#     f.delete()