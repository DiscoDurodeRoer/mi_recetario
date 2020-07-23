from django.db import models

class User(models.Model):
    id = models.AutoField(name="id", primary_key=True)
    nickname = models.CharField(name="nickname", max_length=45)
    password = models.CharField(name="password", max_length=45)