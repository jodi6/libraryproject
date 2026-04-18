from django.db import models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50) # عنوان الكتاب [cite: 174]
    author = models.CharField(max_length=50) # اسم الكاتب [cite: 174]
    price = models.FloatField(default=0.0) # السعر [cite: 174]
    edition = models.SmallIntegerField(default=1) # الطبعة [cite: 175]

