from django import forms


class CreditForm(forms.Form):
    groceries = forms.IntegerField(label='Groceries', min_value=0)
    dining = forms.IntegerField(label='Dining out', min_value=0)
    gas = forms.IntegerField(label='Gas', min_value=0)
    travels = forms.IntegerField(label='Travels', min_value=0)
    etc = forms.IntegerField(label='Everything Else', min_value=0)