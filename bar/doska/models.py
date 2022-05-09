from django.db import models

# Create your models here.

class notice(models.Model):
    text = models.CharField(max_length = 200)
    def __str__(self):
        return self.text

class comment(models.Model):
    notice = models.ForeignKey(notice, on_delete=models.CASCADE)
    text = models.CharField(max_length = 100)
    def __str__(self):
        return self.text
