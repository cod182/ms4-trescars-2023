from django import forms


class email_form(forms.Form):
    recipient = forms.EmailField()
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
