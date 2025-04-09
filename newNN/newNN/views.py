from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PlaceForm, HotelForm, LogForm, PlaceEditForm
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


            if district != '0':
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM places WHERE district = {district}'''
                ).fetchall()]
            else:
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM places'''
                ).fetchall()]
                
                
            out1 = []
            if categories != '0':
                allPl = dateBase.execute(
                    f'''SELECT id, categories FROM places'''
                ).fetchall()
                for pl in allPl:
                    data1 = json.loads(pl[1])
                    if categories in data1:
                        out1.append(pl[0])
            else:
                out1 = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM places'''
                ).fetchall()]
            
            
            out = list(set(out) & set(out1))
            
                
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
            
            
            if district != '0':
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels WHERE district = {district}'''
                ).fetchall()]
            else:
                out = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels'''
                ).fetchall()]
            
            
            out1 = []
            if categories != 0:
                allPl = dateBase.execute(
                    f'''SELECT id, categories FROM hotels'''
                ).fetchall()
                for pl in allPl:
                    data1 = json.loads(pl[1])
                    if categories in data1:
                        out1.append(pl[0])
            else:
                out1 = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels'''
                ).fetchall()]
            
            
            out2 = []
            if stars != 0:
                out2 = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels WHERE stars = {stars}'''
                ).fetchall()]
            else:
                out2 = [j[0] for j in dateBase.execute(
                    f'''SELECT id FROM hotels'''
                ).fetchall()]
                
                
            out = list(set(out1) & set(out) & set(out2))
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
    cont = json.loads(place[4])
    tel = cont['tel'] if 'tel' in cont else ''
    email = cont['email'] if 'email' in cont else ''
    link = cont['link'] if 'link' in cont else ''
    place = list(place) + [tel, email, link] + [img[2:-1]]
    return render(request, 'place_one.html', {'place': place})


def hotelOne(request, id):
    dateBase = DateBase()
    hotel = dateBase.execute(
        f'''SELECT id, name, address, description, contacts, stars, photo_id
                    FROM hotels WHERE id ={id}'''
    ).fetchone()
    img = json.loads(hotel[-1])[0]
    img = dateBase.execute(
        f'''SELECT imgData FROM imgs WHERE id = {img}'''
    ).fetchone()[0]
    cont = json.loads(hotel[4])
    tel = cont['tel'] if 'tel' in cont else ''
    email = cont['email'] if 'email' in cont else ''
    link = cont['link'] if 'link' in cont else ''
    hotel = list(hotel) + [tel, email, link] + [img[2:-1]]
    return render(request, 'place_one.html', {'hotel': hotel})


def admin(request):
    idU = request.COOKIES.get('id', False)
    if idU != '3d5148a1666a59cc27311c96f9a346effaa6beacc4e2e55c6ee23d7ea925b44a':
        return HttpResponseRedirect('/log')
    
    dateBase = DateBase()
    
    #places
    places = dateBase.execute(
        f'''SELECT id, name, description, photo_id
                    FROM places LIMIT 6'''
    ).fetchall()
    for i in range(len(places)):
        img = json.loads(places[i][3])[0]
        img = dateBase.execute(
            f'''SELECT imgData FROM imgs WHERE id = {img}'''
        ).fetchone()[0]
        places[i] = list(places[i]) + [img[2:-1]]
    
    
    #hotels
    hotels = dateBase.execute(
        f'''SELECT id, name, description, stars, photo_id
                    FROM hotels LIMIT 6'''
    ).fetchall()
    for i in range(len(hotels)):
        img = json.loads(hotels[i][-1])[0]
        img = dateBase.execute(
            f'''SELECT imgData FROM imgs WHERE id = {img}'''
        ).fetchone()[0]
        hotels[i] = list(hotels[i]) + [img[2:-1]]
        
    
    return render(request, 'admin.html', {'places': places, 'hotels': hotels})


def log(request):
    
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == 'admin123':
                outt = HttpResponseRedirect('/admin')
                outt.set_cookie("id", '3d5148a1666a59cc27311c96f9a346effaa6beacc4e2e55c6ee23d7ea925b44a', max_age=7 * 24 * 60 * 60)
                return outt
    else:
        form = LogForm()
    return render(request, 'log.html', {'form': form})


def placeEdit(request, id):
    dateBase = DateBase()
    if request.method == 'POST':
        form = PlaceEditForm(request.POST)
        
    else:
        data = list(dateBase.execute(f"""SELECT * FROM places WHERE id={id}""").fetchone())
        cont = json.loads(data[4])
        tel = cont['tel'] if 'tel' in cont else ''
        email = cont['email'] if 'email' in cont else ''
        link = cont['link'] if 'link' in cont else ''
        categories = [json.loads(data[5])[0]]
        form = PlaceEditForm(my_arg = data[1:4] + [tel, email, link] + categories + [data[6]])
        return render(request, 'placeEdit.html', {'form': form})
    

def hotelEdit(request):
    pass