#i created it

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params={'name':"abhinav",'place':"ghaziabad"}
    return render(request,'index.html',params)
def check(request):
    if request.GET.get("capitalall")=="on":
        fname = request.GET.get("firstname")
        lname = request.GET.get("lastname")
        return HttpResponse(fname.upper()+" "+lname.upper())
    if request.GET.get("camelcase")=="on":
        fname = request.GET.get("firstname")
        lname = request.GET.get("lastname")

        return HttpResponse(fname[0].lower() + fname[1:].upper()+" "+lname[0].lower() + lname[1:].upper())

    return HttpResponse("not selected any field")

def number(request):
    if request.GET.get("palandrome")=="on":
        num=str(request.GET.get("number"))
        result=num[::-1]
        for i in range(len(num)):
            if num[i] != result[i]:
                return render(request,'number.html',{'num':'number is not palandrome'})
        return render(request,'number.html',{'num':'number is palandrome'})

    if request.GET.get("armstrong")=="on":
        num=int(request.GET.get("number"))
        result=num
        sum=0
        length=len(str(result))
        while result !=0:
            rem=result%10
            sum+=rem**length
            result//=10
        if sum==num:
            return render(request, 'number.html', {'num': 'number is armstrong'})
        else:
            return render(request, 'number.html', {'num': 'number is not armstrong'})

    if request.GET.get("strong")=="on":
        num=int(request.GET.get("number"))
        result=num
        sum=0
        while result !=0:
            sum1=1
            rem=result%10
            for i in range(1,rem+1):
                sum1*=i
            sum+=sum1

            result//=10
        if sum==num:
            return render(request, 'number.html', {'num': 'number is strong'})
        else:
            return render(request, 'number.html', {'num': 'number is not strong'})


    return HttpResponse("select the field")



