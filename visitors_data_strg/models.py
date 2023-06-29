from django.db import models
import random



# def visitor_directory_path(instance, filename): 
#     name, ext = filename.split(".")
#     name = instance.id_number # + "_" + instance.branch + "_" + instance.year + "_" + instance.section
#     filename = name+'.'+ext 
#     return 'Visitor_Images/{}/{}/{}/{}'.format(instance.id,instance.id_number,instance.first_name,filename)


class Citizen(models.Model):
    id_number = models.CharField(max_length=50, unique=True, default=0)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='citizen/', null=True)

    def __str__(self):
        return self.firstName

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.id_number = random.randint(100000, 999999)
        
        super().save(*args, **kwargs)

