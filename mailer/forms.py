from django import forms


class EmailForm(forms.Form):
    recipient = forms.EmailField()
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
