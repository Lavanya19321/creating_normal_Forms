from django.db import models

# Create your models here.
class schooldata (models.Model):
    uname=models.CharField(max_length=30,primary_key=True)
    sname=models.CharField(max_length=20)
    slocation=models.CharField(max_length=30)
    sprincipal=models.CharField(max_length=30)
    def __str__(self):
        return self.uname
