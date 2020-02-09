from django.shortcuts import render,redirect
from django.http import HttpResponse
from faceofnepal.models import Freelancer,FreelancerForm
from faceofnepal.forms import FreelancerForms

# Create your views here.
def index(requst):
    return HttpResponse("hello world")


def freelancer_form(request):
    return render(request,'Freelancerform.html',)



def freelancer_save(request):
    if request.method== 'POST': 
        get_Name =request.POST['Name']
        get_Address= request.POST['Address']
        get_Phone =request.POST['Phone']
        get_Description= request.POST['Description']
        Freelancer_obj = Freelancer(Name=get_Name,Address=get_Address,Phone=get_Phone,Description=get_Description)
        Freelancer_obj.save()
        return HttpResponse("Save record!!")
    else:
        return HttpResponse("Error record saving!!")


def freelancer_list(request):
    list_of_Freelancers= Freelancer.objects.all()
    context_variable = {
        'Freelancer':list_of_Freelancers
    }
    return render(request,'Freelancer.html',context_variable)

def freelancer_edit(request, ID):
    freelancer_obj = Freelancer.objects.get(id=ID)
    context_varible = {
        'freelancer':freelancer_obj
    }
    return render(request,'FreelancerUpdateForm.html',context_varible)

def freelancer_update_saves(request,ID):
    freelancer_obj = Freelancer.objects.get(id=ID)
    freelancer_form_data = request.POST
    print(freelancer_form_data) 
    freelancer_obj.Name = request.POST['Name']
    freelancer_obj.Address =request.POST['Address']
    freelancer_obj.phone = request.POST['Phone']
    freelancer_obj.Description = request.POST['Description']
    freelancer_obj.save()
    return HttpResponse("Record Updated!!!!")

def freelancer_update_save(request,ID):
    freelancer_obj = Freelancer.objects.get(id=ID)
    form=FreelancerForms(request.POST, instance = freelancer_obj)
    if form.is_valid():
        form.save()
        return redirect("/freelancerlist")
    return render(request,"FreelancerUpdateForm.html",{'freelancer_obj':freelancer_obj})



def freelancer_delete(request,ID):
        freelancer_obj= Freelancer.objects.get(id=ID)
        freelancer_obj.delete()
        return HttpResponse("Record Delete!!")


