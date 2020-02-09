from django.db import models


# Create your models here.
class FreelancerForm(models.Manager):
    pass

class Freelancer(models.Model):
    Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Description = models.TextField(max_length=250)
    objects=FreelancerForm()


    def __str__(self):
     return f"My Name is {self.Name}. I am from {self.Address} and my contact no. {self.Phone}"


class Tourist(models.Model):
    name = models.ForeignKey(Freelancer,on_delete=models.CASCADE,related_name="names")
    address = models.ForeignKey(Freelancer,on_delete=models.CASCADE,related_name="add")
    phone = models.IntegerField()

    # def __str__(self):
    #     return f"I am {self.name.Name} address  {self.address.Address} and {self.phone}"