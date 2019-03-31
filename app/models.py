from django.db import models
from django.urls import reverse

class Students(models.Model):   
    name = models.CharField(blank=False, max_length=50)
    school = models.CharField(blank=False, max_length=50)
    std = models.IntegerField(blank=False)
    roll_no = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    # IN the reverse put the name of url ans id is same as id passes on the url    
    def get_absolute_url(self):
        return reverse("dynamic_view", kwargs={"id": self.id}) #f"/list/{self.id}" 