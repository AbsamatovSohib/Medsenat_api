from django.db import models

class Basemodel(models.Model):

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Sponsor(Basemodel):

    title = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 9)

    choices = (
        ("Yuridik","Yuridik"),
        ("Jismoniy", "Jismoniy"),
        )
    
    person_type = models.CharField(max_length = 10, choices = choices, default = "Jismoniy")
    money = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add = True)

    situation_choice = (("barchasi","barchasi"),("Yangi","Yangi"),("moderatsiyada","moderiyatsiyada"),("tasdiqlangan","tasdiqlangan"),("bekor qilingan","bekor qilingan"))

    situation = models.CharField(max_length = 10, choices = situation_choice, default = "barchasi")

    def __str__(self):
        return self.title[0:10]
    
    class Meta:

        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"


class University(Basemodel):

    title = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.title
    
    class Meta:

        verbose_name = "university"
        verbose_name_plural = "universities"


class Student(Basemodel):

    title = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)


    student_degree = (
        ("bachelor","bachelor"),
        ("master","master"))

    stduent_degree = models.CharField(max_length = 10, choices = student_degree, default = "bachelor")

    contract_price = models.PositiveBigIntegerField()


    def __str__(self) :
        return self.title
    
    class Meta:

        verbose_name = "Student"
        verbose_name_plural = "Students"