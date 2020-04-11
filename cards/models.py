from django.db import models

# Create your models here.

class Card (models.Model): 
	cardName=models.CharField(max_length=200)
	bankName=models.CharField(max_length=200)
	annualFee= models.IntegerField()
	rewardsType=models.CharField(max_length=200)
	rewardValue= models.DecimalField(max_digits=5, decimal_places=5)
	rewardsDisplay= models.TextField()
	groceryMultiplier= models.IntegerField()
	restaurantMultiplier= models.IntegerField()
	travelMultiplier= models.IntegerField()
	otherMultiplier=models.IntegerField()
	gasMultiplier= models.IntegerField()
	everythingElse = models.IntegerField(default=1)
	APR= models.IntegerField()
	bonusDisplay=models.TextField()
	bonusValue= models.IntegerField() 
	link=models.TextField()
	creditScore= models.CharField(max_length=200)

	def __str__(self):
		return self.cardName


