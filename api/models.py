from django.db import models

# Create your models here.



class Sponsor(models.Model):


    title = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 9)

    choices = (
        ("Yuridik","Yuridik"),
        ("Jismoniy", "Jismoniy"),
        )
    
    person_type = models.CharField(max_length = 10, choices = choices, default = "Jismoniy")

    money = models.BigIntegerField()
