from django.db import models

# Create your models here.
class Register(models.Model):
	Name=models.CharField(max_length=20)
	Email=models.EmailField()
	Place=models.CharField(max_length=20)
	Photo=models.ImageField(upload_to='media/')
	Password=models.CharField(max_length=20)

class Gallery(models.Model):
	Photo1=models.ImageField(upload_to='media2/',default='SOME STRING')
	Name=models.CharField(max_length=20)
	Price=models.IntegerField()
	

