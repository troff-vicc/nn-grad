from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PlaceForm, HotelForm
from .sqlite import DateBase
import json

def index(request):
    return render(request, 'home.html')


def place(request):
    dateBase = DateBase()
    
    def check(data, tr):
        data = json.loads(data)
        return tr in data
        
    if request.method == 'POST':
        print(1)
        form = PlaceForm(request.POST)
        dateBase.create_function('CHECK', 2, check)
        categories = form.cleaned_data['allCategories']
        district = form.cleaned_data['allDistrict']
        places = []
        if district != 0:
            print(2)
            places += list(dateBase.execute(
                f'''SELECT id, name, description, photo_id
                            FROM places WHERE district = {district}'''
            ).fetchall())
        if categories != 0:
            print(3)
            places += list(dateBase.execute(
                f'''SELECT id, name, description, photo_id
                                        FROM places WHERE CHECK(categories, '{categories}')'''
            ).fetchall())
        places = list(set(places))
        for i in range(len(places)):
            print(4)
            img = json.loads(places[i][3])[0]
            img = dateBase.execute(
                f'''SELECT imgData FROM imgs WHERE id = {img}'''
            ).fetchone()[0]
            places[i] = list(places[i]) + [img[2:-1]]
        return render(request, 'place.html', {'form': form, 'places': places})
    else:
        form = PlaceForm()
        places = dateBase.execute(
            f'''SELECT id, name, description, photo_id
                FROM places LIMIT 8'''
        ).fetchall()
        for i in range(len(places)):
            img = json.loads(places[i][3])[0]
            img = dateBase.execute(
                f'''SELECT imgData FROM imgs WHERE id = {img}'''
            ).fetchone()[0]
            places[i] = list(places[i])+[img[2:-1]]
        
    return render(request, 'place.html', {'form': form, 'places': places})


def hotel(request):
    dateBase = DateBase()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        categories = form.cleaned_data['allCategories']
        
    else:
        form = HotelForm()
        places = dateBase.execute(
            f'''SELECT id, name, description, stars, photo_id
                FROM hotels LIMIT 8'''
        ).fetchall()
        for i in range(len(places)):
            img = json.loads(places[i][-1])[0]
            img = dateBase.execute(
                f'''SELECT imgData FROM imgs WHERE id = {img}'''
            ).fetchone()[0]
            places[i] = list(places[i]) + [img[2:-1]]
    
    return render(request, 'hotel.html', {'form': form, 'places': places})


def child(request):
    return render(request, 'child.html')

def help(request):
    return render(request, 'help.html')