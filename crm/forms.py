from django import forms

class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'nl-email'}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'nl-email'}))

