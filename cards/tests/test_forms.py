from django.test import TestCase
from ..forms import CreditForm


class CreditFormTest(TestCase):

    # test valid data in the form
    def test_credit_form_valid_data(self):
        data = {
            'groceries': 2,
            'dining': 3,
            'gas': 3,
            'travels': 3,
            'etc': 3,
            'credit_score': 'good',
            'annual': 'no',
            'banks': ['Chase', 'Citibank', 'American Express', 'Capital One'
                        , 'Wells Fargo', 'Bank of America'],
        }

        form = CreditForm(data=data)
        self.assertTrue(form.is_valid())

    # test invalid data in the form
    def test_credit_form_no_data(self):
        form = CreditForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)
