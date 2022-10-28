from django.shortcuts import render

# Create your views here.

def MainPageView(request):
    return render(request,'affairs/index.html',{})