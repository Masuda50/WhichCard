from django import forms


class CreditForm(forms.Form):
    groceries = forms.DecimalField(label='Groceries', min_value=0)
    dining = forms.DecimalField(label='Dining out', min_value=0)
    gas = forms.DecimalField(label='Gas', min_value=0)
    travels = forms.DecimalField(label='Travels', min_value=0)
    etc = forms.DecimalField(label='Everything Else', min_value=0)
