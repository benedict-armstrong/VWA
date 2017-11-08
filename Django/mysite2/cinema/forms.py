from django import forms

class UserIdForm(forms.Form):
    User_id = forms.CharField(label='User ID', max_length=100)