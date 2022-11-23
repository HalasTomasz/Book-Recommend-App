from django.db import models

class UserReview(models.Model):
    Order_ID = models.AutoField(primary_key=True,editable=False)
    Review = models.IntegerField(null=True,blank=True, default=0)
    Books = models.CharField(max_length=255, null = True, blank = True)