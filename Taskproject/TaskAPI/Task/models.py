from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	task_name = models.CharField(max_length=100)
	task_description = models.TextField(max_length=200)
	status = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)

