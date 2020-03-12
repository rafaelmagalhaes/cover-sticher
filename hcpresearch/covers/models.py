from django.db import models


# Create your models here.

class Covers(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True)
    cover_image = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
