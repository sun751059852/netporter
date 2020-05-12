from django.db import models

# Create your models here.
from django.utils import timezone


class Endpoint(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 节点IP
    ip = models.CharField(max_length=15)
    create_time=models.DateTimeField(default=timezone.now)


    def create_endpoint(self):
        self.create_time = timezone.now()
        self.save()

    def __str__(self):
        return self.ip