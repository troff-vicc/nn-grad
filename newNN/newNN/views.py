from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PlaceForm, HotelForm
from .sqlite import DateBase
import json

def index(request):
    return render(request, 'home.html')


def place(request):
    dateBase = DateBase()
        
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['allCategories']
            district = form.cleaned_data['allDistrict']
            places = []
            out = []
            if district == 0 and categories == 0:
                return HttpResponseRedirect('/place')
            if district != 0:
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM places WHERE district = {district}'''
                ).fetchall()]
            if categories != 0:
                allPl = dateBase.execute(
                    f'''SELECT id, categories FROM places'''
                ).fetchall()
                for pl in allPl:
                    data1 = json.loads(pl[1])
                    if categories in data1:
                        out.append(pl[0])
            out = list(set(out))
            for i in out:
                places.append(list(dateBase.execute(
                    f'''SELECT id, name, description, photo_id
                                            FROM places WHERE id = {i}'''
                ).fetchone()))
            for i in range(len(places)):
                img = json.loads(places[i][-1])[0]
                img = dateBase.execute(
                    f'''SELECT imgData FROM imgs WHERE id = {img}'''
                ).fetchone()[0]
                places[i] = list(places[i]) + [img[2:-1]]
            return render(request, 'place.html', {'form': form, 'places': places})
        else:
            return HttpResponseRedirect('/place')
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
        form = HotelForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['allCategories']
            district = form.cleaned_data['allDistrict']
            stars = form.cleaned_data['allStars']
            hotels = []
            out = []
            if district == 0 and categories == 0 and stars == 0:
                return HttpResponseRedirect('/hotel')
            if district != 0:
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels WHERE district = {district}'''
                ).fetchall()]
            if categories != 0:
                allPl = dateBase.execute(
                    f'''SELECT id, categories FROM hotels'''
                ).fetchall()
                for pl in allPl:
                    data1 = json.loads(pl[1])
                    if categories in data1:
                        out.append(pl[0])
            if stars != 0:
                out += [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels WHERE stars = {stars}'''
                ).fetchall()]
            out = list(set(out))
            for i in out:
                hotels.append(list(dateBase.execute(
                    f'''SELECT id, name, description, stars, photo_id
                                            FROM hotels WHERE id = {i}'''
                ).fetchone()))
            for i in range(len(hotels)):
                img = json.loads(hotels[i][-1])[0]
                img = dateBase.execute(
                    f'''SELECT imgData FROM imgs WHERE id = {img}'''
                ).fetchone()[0]
                hotels[i] = list(hotels[i]) + [img[2:-1]]
            return render(request, 'hotel.html', {'form': form, 'hotels': hotels})
        else:
            return HttpResponseRedirect('/hotel')
        
    else:
        form = HotelForm()
        hotels = dateBase.execute(
            f'''SELECT id, name, description, stars, photo_id
                FROM hotels LIMIT 8'''
        ).fetchall()
        for i in range(len(hotels)):
            img = json.loads(hotels[i][-1])[0]
            img = dateBase.execute(
                f'''SELECT imgData FROM imgs WHERE id = {img}'''
            ).fetchone()[0]
            hotels[i] = list(hotels[i]) + [img[2:-1]]
    
    return render(request, 'hotel.html', {'form': form, 'hotels': hotels})


def child(request):
    return render(request, 'child.html')

def help(request):
    return render(request, 'help.html')


def placeOne(request, id):
    dateBase = DateBase()
    place = dateBase.execute(
        f'''SELECT id, name, address, description, contacts, photo_id
                    FROM places WHERE id ={id}'''
    ).fetchone()
    img = json.loads(place[-1])[0]
    img = dateBase.execute(
        f'''SELECT imgData FROM imgs WHERE id = {img}'''
    ).fetchone()[0]
    place = list(place) + [img[2:-1]]
    return render(request, 'place_one.html', {'place': place})