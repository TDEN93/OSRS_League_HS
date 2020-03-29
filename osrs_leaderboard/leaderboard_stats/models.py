from django.db import models

class league_hiscores(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    exp = models.IntegerField()