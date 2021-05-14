from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    roll= models.CharField(max_length=18)
    email= models.EmailField(max_length=20)
    password= models.CharField(max_length=20)
   #gender= models.TextChoices()
    phone= models.CharField(max_length=12)
    #dob= models.DateField(default='')
    address= models.TextField()

    def __str__(self):
        return self.name