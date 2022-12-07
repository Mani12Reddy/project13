from django.shortcuts import render

# Create your views here.
def mani(request):
    return render(request,'mani.html')

def mani2(request):
    return render(request,'mani2.html')
