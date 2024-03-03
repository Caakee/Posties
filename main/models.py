from django.db import models
 
# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    username = models.CharField(max_length=300)
    userID = models.IntegerField()
    log_date = models.DateTimeField("date logged")
 
    class Meta:  
        db_table = "tblevents"