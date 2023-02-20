from django.db import models

# Create your models here.

class CallList(models.Model):
    id = models.AutoField(primary_key=True)
    from_number = models.CharField(max_length=50)
    to_number = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add = True)
