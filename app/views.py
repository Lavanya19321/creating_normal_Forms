from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        Username=request.POST['un']
        return HttpResponse(Username)
    
    return render(request,'htmlforms.html')

def schoolrecord(request):
    if request.method=='POST':
        un=request.POST['un']
        sn=request.POST['sn']
        sl=request.POST['sl']
        sp=request.POST['sp']
        SO=schooldata.objects.get_or_create(uname=un,sname=sn,slocation=sl,sprincipal=sp)[0]
        SO.save()
        return HttpResponse('data inserted successfully')
    return render(request,'schoolrecord.html')