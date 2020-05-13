from django.db import models
from django.utils import timezone
# Create your models here.


class Card (models.Model):
	cardName=models.CharField(max_length=200)
	bankName=models.CharField(max_length=200)
	annualFee= models.IntegerField()
	rewardsType=models.CharField(max_length=200)
	rewardValue= models.DecimalField(max_digits=10, decimal_places=5)
	rewardsDisplay= models.TextField()
	groceryMultiplier= models.DecimalField(max_digits=10, decimal_places=5)
	restMultiplier= models.DecimalField(max_digits=10, decimal_places=5)
	travelMultiplier= models.DecimalField(max_digits=10, decimal_places=5)
	gasMultiplier= models.DecimalField(max_digits=10, decimal_places=5)

	elseMultiplier=models.DecimalField(max_digits=10, decimal_places=5, default=0)
	APR= models.DecimalField(max_digits=10, decimal_places=5, default=1)
	bonusDisplay=models.TextField(blank=True,null=True)

	bonusValue= models.IntegerField(default=1)
	link=models.TextField()
	creditScore= models.CharField(max_length=200)
	bonusMinimumSpend=models.IntegerField()
	bonusSpendMonths=models.IntegerField()

	# values will be used to inform the user about the last DB update
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.cardName
