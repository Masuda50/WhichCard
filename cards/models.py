from django.db import models

# Create your models here.

class Card (models.Model): 
	cardName=models.CharField(max_length=200)
	bankName=models.CharField(max_length=200)
	annualFee= models.IntegerField()
	rewardsType=models.CharField(max_length=200)
	rewardValue= models.IntegerField()
	rewardsDisplay= models.TextField()
	groceryMultiplier= models.IntegerField()
	restMultiplier= models.IntegerField()
	travelMultiplier= models.IntegerField()
	otherMultiplier=models.IntegerField()
	gasMultiplier= models.IntegerField()
	valOfSingRe= models.IntegerField()
	APR= models.IntegerField()
	bonusDisplay=models.TextField()
	bonusValue= models.IntegerField() 
	link=models.TextField()
	creditScore= models.IntegerField()



