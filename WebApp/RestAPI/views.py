from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from faceofnepal.models import Freelancer
import json

@csrf_exempt
def view_get_post_freelancer(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        freelancers = Freelancer.objects.all()
        print("QuerySet objects => ",freelancers)
        list_of_freelancers = list(freelancers.values("Name","Address","Phone","Description"))
        print("List of Airport objects => ",list_of_freelancers)
        dictionary_name = {
        "freelancers":list_of_freelancers
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['Name'])
        print(python_dictionary_object['Address'])
        print(python_dictionary_object['Phone'])
        print(python_dictionary_object['Description'])

        Freelancer.objects.create(Name=python_dictionary_object['Name'],Address=python_dictionary_object['Address'],Phone=python_dictionary_object['Phone'],Description=python_dictionary_object['Description'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        freelancer = Freelancer.objects.get(id = ID)
        print(type(freelancer.Name))
        return JsonResponse({
            "id":freelancer.id,
            "Name":freelancer.Name,
            "Address":freelancer.Address,
            "Phone":freelancer.Phone,
            "Description":freelancer.Description
        })

    elif request.method=="PUT":
        guide=Freelancer.objects.get(id=ID)
        python_dict_object = json.loads(request.body)
        guide.Name=python_dict_object['Name']
        guide.Address=python_dict_object['Address']
        guide.Phone=python_dict_object['Phone']
        guide.Description=python_dict_object['Description']
        guide.save()
        return JsonResponse({
        "message":" update your put data successfully!!!"
        })
    
    elif request.method=="DELETE":
        guide=Freelancer.objects.get(id=ID)
        guide.delete()
        return JsonResponse({
        "message":" delete id successfully!!!!!!!!!1"
        })


