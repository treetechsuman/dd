from django.shortcuts import render

from address.models import District, Province, Municipality

# Create your views here.
def index(request):
    provinces = Province.objects.all()
    districts = District.objects.all()
    municipalities = Municipality.objects.all()
    
    context={
        'provinces':provinces,
        'districts':districts,
        'municipalities':municipalities
    }
    return render(request,'address/index.html',context)