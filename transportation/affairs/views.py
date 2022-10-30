from django.shortcuts import render
from .models import CourierModel, CustomerModel
from .forms import CourierForm, CustomerForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from affairs import views
from django.contrib.auth.decorators import login_required

# Create your views here.


def MainPageView(request):
    return render(request,'affairs/index.html',{})
    

@login_required
def CourierListView(request):
    couriers = CourierModel.objects.all()

    context = {
        'courier': couriers
    }

    return render(request,'affairs/CourierList.html',context)

@login_required
def CourierCreateView(request):
    if request.method == 'POST':
        courierForm = CourierForm(request.POST)
        if courierForm.is_valid:
            courierForm.save()
            return HttpResponseRedirect(reverse(views.CourierListView))
    else:
        courierForm = CourierForm()

    context = {
        'coForm': courierForm
    }

    return render(request,'affairs/CourierCreate.html',context)

@login_required
def CourierUpdateView(request,id):
    cInstance = CourierModel.objects.get(pk=id)
    if request.method == 'POST':
        courierForm = CourierForm(request.POST,instance=cInstance)
        if courierForm.is_valid:
            courierForm.save()
            return HttpResponseRedirect(reverse(views.CourierListView))
    else:
        courierForm = CourierForm(instance=cInstance)

    context = {
        'coForm': courierForm
    }

    return render(request,'affairs/CourierUpdate.html',context)

@login_required
def CourierDeleteView(request,id):
    cInstance = CourierModel.objects.get(pk=id)
    cInstance.delete()
    return HttpResponseRedirect(reverse(views.CourierListView))
    

@login_required
def CustomerListView(request):
    customers = CustomerModel.objects.all()

    context = {
        'customers': customers
    }
    return render(request,'affairs/CustomerList.html',context)


def CustomerCreateView(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid:
            customerForm.save()
            return HttpResponseRedirect(reverse(views.CustomerListView))
    else:
        customerForm = CustomerForm()

    context = {
        'cForm': customerForm
    }

    return render(request,'affairs/CustomerCreate.html',context)

@login_required
def CustomerUpdateView(request,id):
    cInstance = CustomerModel.objects.get(pk=id)
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST,instance=cInstance)
        if customerForm.is_valid:
            customerForm.save()
            return HttpResponseRedirect(reverse(views.CustomerListView))
    else:
        customerForm = CustomerForm(instance=cInstance)

    context = {
        'cForm': customerForm
    }

    return render(request,'affairs/CustomerUpdate.html',context)

@login_required
def CustomerDeleteView(request,id): 
    try:   
        cInstance = CustomerModel.objects.get(pk=id)
        cInstance.delete()
        return HttpResponseRedirect(reverse(views.CustomerListView))
    except:
        return HttpResponse('Integrity Problem')