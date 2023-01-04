from django.shortcuts import render

# Create your views here.
def temp(request):
    d={'a':100,'b':200,'c':70}
    return render(request,'temp.html',d)