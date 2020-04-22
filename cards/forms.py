from django import forms

CREDIT_CHOICES = [('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('bad', 'Bad')]
ANNUAL_CHOICES = [('yes', 'Yes'), ('no', 'No')]
BANK_CHOICES   = [('chase', 'Chase'), ('citi', 'Citibank'), ('amex', 'American Express'), ('capital one', 'Capital One'), ('wells fargo','Wells Fargo'), ('bank of america', 'Bank of America'), ('all', 'All of the Above')]


class CreditForm(forms.Form):
    groceries = forms.DecimalField(label='Groceries', min_value=0)
    dining = forms.DecimalField(label='Dining out', min_value=0)
    gas = forms.DecimalField(label='Gas', min_value=0)
    travels = forms.DecimalField(label='Travels', min_value=0)
    etc = forms.DecimalField(label='Everything Else', min_value=0)
    credit_score = forms.CharField(label='What is your credit score?', widget= forms.Select(choices= CREDIT_CHOICES))
    annual= forms.ChoiceField(label='Are you only interested in cards with no annual fee?', widget= forms.RadioSelect, choices= ANNUAL_CHOICES)
    # banks = forms.ModelMultipleChoiceField(label= 'Show cards from the following banks:', widget= forms.CheckboxSelectMultiple, choices= BANK_CHOICES)
