from django.shortcuts import render
from app.forms import *
from app.models import *
# Create your views here.
def studentform(request):
    SDO=student()
    d={'SDO':SDO}
    if request.method=='POST':
        SFO=student(request.POST)
        if SFO.is_valid():
            sid=SFO.cleaned_data['sid']
            name=SFO.cleaned_data['name']
            email=SFO.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,name=name,email=email)[0]
            SO.save()
            SQS=Student.objects.all()
            d1={'SQS':SQS}
            return render(request,'retrieve.html',d1)
    return render(request,'djinsert.html',d)