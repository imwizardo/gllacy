from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    text = forms.CharField(max_length=1000)

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100)

class FilterForm(forms.Form):
    FILLER_CHOICES = [
        ('chocolate', 'Шоколадные'),
        ('sugar_sprinkles', 'Сахарные присыпки'),
        ('fruits', 'Фрукты'),
        ('syrups', 'Сиропы'),
        ('jams', 'Джемы'),
    ]
    fat = forms.CharField(max_length=20, required=False)
    fillers = forms.MultipleChoiceField(choices=FILLER_CHOICES, required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)

