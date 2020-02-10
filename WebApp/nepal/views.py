from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from faceofnepal.models import Freelancer
from django.db.models import Q

# Create your views here.
def index5(request):
   return render(request, 'index5.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def search(request):
    return render(request, 'index5.html')

def searchresults(request):
    query = request.POST['input']
    results = Freelancer.objects.filter(Q(Name__icontains=query) | Q(Address__icontains=query) | Q(Phone__icontains=query))
    Context = {'results': results}
    return render(request, 'searchlist.html', Context)