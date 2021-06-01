from django.db import models


# Create your models here.
class Customerdb(models.Model):
	cuid = models.IntegerField(null=True)
	cuname = models.CharField(max_length=70)
	cumail = models.EmailField(max_length=50)
	cupass = models.CharField(max_length=50,null=True)
	Discription = models.TextField(max_length=200)
	pubdate = models.DateField(primary_key=True)

	def __str__(self):
		return self.cuname
		
class Task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(primary_key=True)
	def __str__(self):
		return self.title
