from django import forms

class AppForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=50)
