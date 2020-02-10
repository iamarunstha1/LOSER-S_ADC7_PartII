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


class Payment(models.Model):
    Cash=models.IntegerField()  
    Cheque=models.CharField(max_length=30)

    # def __str__(self):
    #     return "{self.Cash,self.Cheque}"

class Visitor(models.Model):
    Guide=models.ManyToManyField(Freelancer,blank=True,related_name="guide")
    Visitor_Name=models.CharField(max_length=20)
    Visitor_Email=models.EmailField(max_length=30)
    Visitor_Mobile_No=models.IntegerField()
    Visitor_address=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Guide,self.Visitor_Name,self.Visitor_Email,self.Visitor_Mobile_No,self.Visitor_address}"


class Business(models.Model):
    company_name=models.CharField(max_length=20)
    company_location=models.CharField(max_length=20)
    package_name=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.company_name,self.company_location,self.package_name}"

class Administrator(models.Model):
    admin=models.ForeignKey(Freelancer,on_delete=models.CASCADE,related_name='admin' )
    Guide=models.OneToOneField(Freelancer,  on_delete = models.CASCADE, primary_key = False,related_name='admin_guide')
    Username=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Username,self.admin,self.Guide}" 








