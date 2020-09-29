from django.shortcuts import render, HttpResponseRedirect
from .forms import StaffRegistration
from .models import CreateStaff


# Create your views here.

def index(request):
    if request.method == 'POST':
        forms = StaffRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/')
        else:
            print('form invalid')
    else:
        forms = StaffRegistration()
    staff = CreateStaff.objects.all()
    return render(request, 'enrollStaff/addAndViewStaff.html', {'staff': staff})


def deleteStaff(request,id):
    if request.method == 'POST':
        pi = CreateStaff.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')


def addAndViewStaff(request):
    return render(request, 'enrollStaff/addAndViewStaff.html')


def updateStaff(request):
    return render(request, 'enrollStaff/updateStaff.html')


def viewProfileStaff(request):
    return render(request, 'enrollStaff/viewProfileStaff.html')
