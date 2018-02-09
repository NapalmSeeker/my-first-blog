from django.db import models

class Store(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField(max_length=1000)
	price = models.CharField(max_length=10)
	def __str__(self):
		return self.name