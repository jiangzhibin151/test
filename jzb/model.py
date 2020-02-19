from django.db import models

class Test(models.Model):
    user = models.CharField(primary_key=True, max_length=100, default='8080')
    score = models.CharField(max_length=10000000, default=0)

    def __str__(self):
        return self.user + self.score
