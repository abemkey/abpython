from django.shortcuts import render

# Create your views here.
def think(request):
    return render(request,'work.html')