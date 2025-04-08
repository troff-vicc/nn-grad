from django import forms

class PlaceForm(forms.Form):
    categories = ((0, "Все категории"), (1, "Парки"), (2, "Музеи"))
    district = ((0, "Все районы"), (1, "Московский"), (2, "Ленинский"))
    
    allCategories = forms.ChoiceField(choices = categories, label_suffix=False, label='',)
    allDistrict = forms.ChoiceField(choices = district, label_suffix=False, label='',)