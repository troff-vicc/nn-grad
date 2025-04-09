from django import forms

class PlaceForm(forms.Form):
    categories = ((0, "Все категории"), (1, "Парки"), (2, "Музеи"))
    district = ((0, "Все районы"), (1, "Московский"), (2, "Ленинский"))
    
    allCategories = forms.ChoiceField(choices = categories, label_suffix=False, label='')
    allDistrict = forms.ChoiceField(choices = district, label_suffix=False, label='')
    
    
class HotelForm(forms.Form):
    categories = ((0, "Все категории"), (1, "Хостелы"), (2, "Отели"), (3, "Гостиницы"))
    district = ((0, "Все районы"), (1, "Московский"), (2, "Ленинский"))
    stars = ((0, "Все звёзды"), (1, "⭐️"), (2, "⭐️⭐️"), (3, "⭐️️️️️️️️⭐️⭐️"), (4, "⭐️️️️️️️️️⭐️⭐️⭐️"), (5, "⭐⭐️⭐️️️️️️️️️⭐️⭐️️"))
    
    allCategories = forms.ChoiceField(choices = categories, label_suffix=False, label='')
    allDistrict = forms.ChoiceField(choices = district, label_suffix=False, label='')
    allStars = forms.ChoiceField(choices=stars, label_suffix=False, label='')
    

class LogForm(forms.Form):
    code = forms.CharField(label_suffix=False, label='', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'Код админа',
                                                         'autocomplete': "off"}))
