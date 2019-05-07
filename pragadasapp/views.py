from django.shortcuts import render

from.models import Progadas,ChooseFile
from django.http.response import HttpResponse
def home_view(request):
    return render(request,'home.html')

def pragadas_view(request):
    if request.method=="POST":
        date=request.POST.get('date')
        name=request.POST.get('name')
        num=request.POST.get('num')
        num2=request.POST.get('num2')
        email=request.POST.get('email')
        Progadas(
            date=date,
            customer_name=name,
            prodect_order=num,
            cus_amount=num2,
            email=email,

        ).save()
        data = Progadas.objects.all()
        print(data)

        return render(request,'pragadas.html',{'data':data})


    else:
        # return HttpResponse("insert data")
        data = Progadas.objects.all()

        return render(request,'pragadas.html',{'data':data})


def choose_view(request):
    if request.method == "POST":
        file = request.POST.get('file', '')
        data=ChooseFile(
            choose_file=file,
        )
        data.save()



         # return HttpResponse("insert data")

        return render(request, 'choosefile.html')

    else:
       return render(request,'choosefile.html')


def views_view(request):
    val=Progadas.objects.all()
    print(val)

    return render(request,'view.html',{"data":val})