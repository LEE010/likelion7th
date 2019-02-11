from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField("data published")
    body = models.TextField()
