from django.db import models
from accounts.models import Reception



class Visitor(models.Model):
    first_name = models.CharField(null=True, max_length=50)
    middle_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    gender = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=True, max_length=50)
    office_visited = models.CharField(null=True, max_length=50)
    purpose = models.CharField(null=True, max_length=50)
    guest_from = models.CharField(null=True, max_length=50)
    vendor = models.ForeignKey("accounts.User",null=True, on_delete=models.CASCADE)
    reception_by = models.ForeignKey(Reception,null=True, on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)
    date_visited = models.DateField(auto_now=True)
    in_time = models.TimeField(auto_now=True)
    out_time = models.TimeField(null=True)
    visitor_image = models.ImageField(upload_to='visitors/', null=True)

    def __str__(self):
        return self.first_name
    


