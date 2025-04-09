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
    
    
class PlaceEditForm(forms.Form):
    name = forms.CharField(label_suffix=False, label='', max_length=100)
    
    description = forms.CharField(label_suffix=False, label='', max_length=1000)
    
    address = forms.CharField(label_suffix=False, label='', max_length=100)
    
    tel = forms.CharField(label_suffix=False, label='', max_length=100)
    
    email = forms.CharField(label_suffix=False, label='', max_length=100)
    
    link = forms.CharField(label_suffix=False, label='', max_length=100)
    
    categories = ((0, "Все категории"), (1, "Парки"), (2, "Музеи"))
    district = ((0, "Все районы"), (1, "Московский"), (2, "Ленинский"))
    
    allCategories = forms.ChoiceField(choices=categories, label_suffix=False, label='')
    allDistrict = forms.ChoiceField(choices=district, label_suffix=False, label='')
    
    img_file = forms.ImageField(label_suffix=False, label='', max_length=255)
    
    def __init__(self, *args, **kwargs):
        t = False
        if kwargs:
            t = True
            my_arg = kwargs.pop('my_arg')
        super(PlaceEditForm, self).__init__(*args, **kwargs)
        if t:
            self.fields['name'].widget = forms.TextInput(attrs={'value': my_arg[0]})
            self.fields['description'].widget = forms.TextInput(attrs={'value': my_arg[2]})
            self.fields['address'].widget = forms.TextInput(attrs={'value': my_arg[1]})
            self.fields['tel'].widget = forms.TextInput(attrs={'value': my_arg[3]})
            self.fields['email'].widget = forms.TextInput(attrs={'value': my_arg[4]})
            self.fields['link'].widget = forms.TextInput(attrs={'value': my_arg[5]})
            self.initial['allCategories'] = my_arg[6]
            self.initial['allDistrict'] = my_arg[7]
