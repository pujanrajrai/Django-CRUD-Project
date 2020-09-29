from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'enrollStaff/addAndViewStaff.html')

def addAndViewStaff(request):
    return render(request, 'enrollStaff/addAndViewStaff.html')

def updateStaff(request):
    return render(request,'enrollStaff/updateStaff.html')

def viewProfileStaff(request):
    return render(request,'enrollStaff/viewProfileStaff.html')

