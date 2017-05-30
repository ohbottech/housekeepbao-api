from django.db import models


# Create your models here.
class Cleaner(models.Model):
    name = models.TextField()
    phone = models.IntegerField()
    email = models.TextField()
    password = models.CharField(max_length=50)
    gender = models.TextField()
    description = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cleaner"