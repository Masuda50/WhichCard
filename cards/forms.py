from django import forms

CREDIT_CHOICES = [('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('bad', 'Bad')]
ANNUAL_CHOICES = [('yes', 'Yes'), ('no', 'No')]
BANK_CHOICES = [('Chase', 'Chase'), ('Citibank', 'Citibank'), ('American Express', 'American Express'),
                ('Capital One', 'Capital One'), ('Wells Fargo', 'Wells Fargo'), ('Bank of America', 'Bank of America'),
                ('all', 'All of the Above')]
CATEGORY_CHOICES = [('credit card', 'CreditCard'), ('bug', 'Bug')]


class CreditForm(forms.Form):
    groceries = forms.DecimalField(label='Groceries', min_value=0,
                                   widget=forms.NumberInput(attrs={'style': 'width:300px'}))
    dining = forms.DecimalField(label='Dining out', min_value=0,
                                widget=forms.NumberInput(attrs={'style': 'width:300px'}))
    gas = forms.DecimalField(label='Gas', min_value=0, widget=forms.NumberInput(attrs={'style': 'width:300px'}))
    travels = forms.DecimalField(label='Travels', min_value=0, widget=forms.NumberInput(attrs={'style': 'width:300px'}))
    etc = forms.DecimalField(label='Everything Else', min_value=0,
                             widget=forms.NumberInput(attrs={'style': 'width:300px'}))
    credit_score = forms.CharField(label='What is your credit score?',
                                   widget=forms.Select(choices=CREDIT_CHOICES, attrs={'style': 'width:300px'}))
    annual = forms.ChoiceField(label='Are you only interested in cards with no annual fee?', widget=forms.RadioSelect,
                               choices=ANNUAL_CHOICES, initial='no')
    banks = forms.MultipleChoiceField(label='Show cards from the following banks:', widget=forms.CheckboxSelectMultiple,
                                      choices=BANK_CHOICES, initial='all')


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'style': 'width:300px'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'style': 'width:300px'}))
    category = forms.ChoiceField(label='Select Issue', widget=forms.RadioSelect,
                                 choices=CATEGORY_CHOICES, initial='no')
    subject = forms.CharField(required=False,widget=forms.TextInput(attrs={'style': 'width:300px'}))
    body = forms.CharField(widget=forms.Textarea)
