from django.db import models


class Client(models.Model):
    class Profession(models.TextChoices):
        student = "etudiant",("etidiant")
        worker = "travailleur",("travailleur")

    name = models.CharField(max_length=155)
    phone = models.PositiveBigIntegerField()
    profession = models.CharField(max_length=155,choices=Profession.choices, default=Profession.student)
    date_enregistrement = models.DateField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=155)


class Service(models.Model):
    name = models.CharField(max_length=155)
    prix = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")





