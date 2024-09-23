from django.db import models


class RemoteSport(models.Model):
    remote_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255)
    sort_order = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)

    process = models.BooleanField(default=False)
    local_sport = models.ForeignKey('usage.Category', blank=True, null=True, on_delete=models.SET_NULL)


class League(models.Model):
    geo_category_id = models.PositiveIntegerField()
    remote_id = models.PositiveIntegerField()
    remote_sport = models.ForeignKey(RemoteSport, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    region_id = models.PositiveIntegerField()
    sort_order = models.CharField(max_length=255)


