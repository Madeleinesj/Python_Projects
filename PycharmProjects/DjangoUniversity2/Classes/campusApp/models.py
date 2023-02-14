from django.db import models


# creates model of University Classes
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state_location = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=True, blank=True, default="")

    # Creates model manager
    object = models.Manager()

    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name}: {0.state_location}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"


