from django.test import TestCase
from ..models import Card


class CardModelTest(TestCase):

	# create new card entry for test cases
	def setUp(self):
		self.card = Card(
			cardName="Chase Freedom",
			bankName="Chase Bank",
			annualFee=0,
			rewardsType="Cash Back",
			rewardValue=0.01,
			rewardsDisplay="5% cash back on select categories",
			groceryMultiplier=2,
			restMultiplier=2,
			travelMultiplier=2,
			gasMultiplier=2,
			elseMultiplier=1,
			APR=2,
			bonusDisplay="dd",
			bonusValue=2,
			link="Chase.com",
			creditScore=2,
			bonusMinimumSpend=1,
			bonusSpendMonths=1,
			created_at="May 13, 2020 7:44 p.m.",
			updated_at="May 13, 2020 7:44 p.m.")

		self.card.save()

	# test model str function
	def test_card_string_function(self):
		self.assertEqual(self.card.__str__(), self.card.cardName)
