from django.db import models


class Basemodel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Sponsor(Basemodel):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)

    choices = (
        ("Yuridik", "Yk"),
        ("Jismoniy", "Jy"),
    )

    person_type = models.CharField(max_length=10, choices=choices)

    money = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    situation_choice = (
        ("barchasi", "barchasi"),
        ("Yangi", "Yangi"),
        ("moderatsiyada", "moderiyatsiyada"),
        ("tasdiqlangan", "tasdiqlangan"),
        ("bekor qilingan", "bekor qilingan"),
    )

    situation = models.CharField(
        max_length=14, choices=situation_choice, default="barchasi"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"


class University(Basemodel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "university"
        verbose_name_plural = "universities"


class Student(Basemodel):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    student_degree = (("bachelor", "bachelor"), ("master", "master"))

    stduent_degree = models.CharField(
        max_length=10, choices=student_degree, default="bachelor"
    )

    contract_price = models.PositiveBigIntegerField()

    student_univercity = models.ForeignKey(
        University, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Donation(Basemodel):
    fromSponsor = models.ForeignKey(
        Sponsor, on_delete=models.CASCADE, blank=True, null=True
    )
    toStudent = models.ForeignKey(
        Student, on_delete=models.CASCADE, blank=True, null=True
    )

    money_rate = models.BigIntegerField()

    def __str__(self):
        return f"{self.toStudent}"
