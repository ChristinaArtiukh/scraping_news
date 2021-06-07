from django import forms


class SendURLForm(forms.Form):
    name = forms.SlugField(max_length=150)
