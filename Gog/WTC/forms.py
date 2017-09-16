from django import forms

class AddFrom(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

