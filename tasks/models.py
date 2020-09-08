from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name