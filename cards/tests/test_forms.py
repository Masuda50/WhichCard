from django.test import TestCase
from ..forms import CreditForm, FeedbackForm


class CreditFormTest(TestCase):

    # test valid data in the form
    def test_credit_form_valid_data(self):
        data = {
            'groceries': 2,
            'dining': 3,
            'gas': 3,
            'travels': 3,
            'etc': 3,
            'credit_score': 'Good',
            'annual': 'yes',
            'banks': ['Chase', 'Citibank', 'American Express', 'Capital One', 'Wells Fargo', 'Bank of America','all'],
        }

        form = CreditForm(data=data)
        self.assertTrue(form.is_valid())

    # test invalid data in the form
    def test_credit_form_no_data(self):
        form = CreditForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)

    def test_feedback_form_valid_data(self):
        data = {
            'name': 'Bob Billy',
            'email': 'test@email.com',
            'category': 'bug',
            'subject': 'stuff',
            'body': 'testing',
        }
        form = FeedbackForm(data=data)
        self.assertTrue(form.is_valid())

    def test_feedback_form_no_data(self):
        form = FeedbackForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
