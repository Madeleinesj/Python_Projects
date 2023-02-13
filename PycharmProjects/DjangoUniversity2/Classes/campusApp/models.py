from django.db import models


# creates model of University Classes
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state_location = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default="")

    # Creates model manager
    object = models.Manager()

    class Meta:
        verbose_name_plural = "University Campus"
