from django.db import models


# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)


class MyApp(models.Model):
    name = models.CharField(max_length=20)
    psw = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.name)
