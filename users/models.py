from django.db import models
# from datetime import datetime


class users(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    eddress = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)

    def __unicode__(self):
        return self.first_name
        return self.last_name
        return self.eddress
        return self.timestamp
