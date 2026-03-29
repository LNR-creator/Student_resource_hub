from django.db import models

class AI_Links(models.Model):
    category = models.CharField(max_length=100)
    website_name = models.CharField(max_length=200)
    website_link = models.URLField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.website_name