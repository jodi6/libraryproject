from django.db import models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50) # عنوان الكتاب [cite: 174]
    author = models.CharField(max_length=50) # اسم الكاتب [cite: 174]
    price = models.FloatField(default=0.0) # السعر [cite: 174]
    edition = models.SmallIntegerField(default=1) # الطبعة [cite: 175]

# جدول العناوين [cite: 94]
class Address(models.Model):
    city = models.CharField(max_length=100) # [cite: 97]

# جدول الطلاب [cite: 85]
class Student(models.Model):
    name = models.CharField(max_length=100) # [cite: 93]
    age = models.IntegerField() # [cite: 93]
    # الربط مع جدول العناوين كـ Foreign Key [cite: 93]
    address = models.ForeignKey(Address, on_delete=models.CASCADE)