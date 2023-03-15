from django.shortcuts import render

# Create your views here.
def condition1(request):
    d={'a':20,'b':40}
    return render(request,'condition1.html',context=d)


def condition2(request):
    d={'a':20,'b':40,'c':30}
    return render(request,'condition2.html',context=d)




def loops(request):
    d={'name':'koti'}
    return render(request,'loops.html',d)