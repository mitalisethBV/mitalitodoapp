from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Task(models.Model):
    s = ((1,"completed"),(2,"pending"))
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250,null=True,default="pending", choices=s)


    #def was_published_recently(self):
    #   return self.time >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.time <= now

    def __str__(self):
        return self.taskTitle
    