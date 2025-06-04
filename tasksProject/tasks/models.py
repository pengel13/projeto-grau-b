from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=150, null=False)
    status = models.CharField(max_length=20, null=False, default="Pending")


class Task_User(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hoursTaken = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["task", "user"], name="task_user_keys")
        ]
