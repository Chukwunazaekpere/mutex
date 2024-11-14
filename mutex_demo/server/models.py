from django.db import models


class Logs(models.Model):
    operation = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_created=True, auto_now_add=True)
    user_type = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=25)
    def __str__(self):
        return self.operation
    
    class Meta:
        get_latest_by = "date_created"