from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PlaceForm
from .sqlite import DateBase
import json

def index(request):
    return render(request, 'home.html')


def place(request):
    dateBase = DateBase()
    if request.method == 'POST':
        return HttpResponseRedirect('/place')
        #form = PlaceForm(request.POST)
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