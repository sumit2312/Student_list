from django.db import models
from django.urls import reverse

class Students(models.Model):   
    name = models.CharField(blank=False, max_length=50)
    school = models.CharField(blank=False, max_length=50)
    std = models.IntegerField(blank=False)
    roll_no = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Students:Students", kwargs={"pk": self.pk})