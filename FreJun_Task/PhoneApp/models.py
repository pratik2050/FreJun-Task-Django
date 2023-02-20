from django.db import models

# Create your models here.

class CallList(models.Model):
    id = models.AutoField(primary_key=True)
    from_number = models.CharField(max_length=12)
    to_number = models.CharField(max_length=12)
    start_time = models.DateTimeField()
