from django import forms

class postform(forms.Form):
    title = forms.CharField(max_length=10)
    text = forms.CharField(widget=forms.Textarea)
    is_enable = forms.BooleanField()
    publish_date = forms.DateField()