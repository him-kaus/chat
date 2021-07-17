from django import forms

class CHATFORM(forms.Form):
    """This is the form where the user inputs chat messages ."""
    message = forms.CharField(required=False,label='',widget=forms.TextInput(attrs={'class' : 'form-control'}))

   
