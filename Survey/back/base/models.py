from django.db import models

class UserReview(models.Model):
    Order_ID = models.AutoField(primary_key=True,editable=False)
    Review1 = models.IntegerField(null=True,blank=True, default=0)
    Review2 = models.IntegerField(null=True,blank=True, default=0)
    Books = models.CharField(max_length=255, null = True, blank = True)
    Date_Taken =  models.DateTimeField(auto_now_add=True)