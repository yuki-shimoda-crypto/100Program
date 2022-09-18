from django import forms

class SentenceForm(forms.Form):
    sentence = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'})
    )