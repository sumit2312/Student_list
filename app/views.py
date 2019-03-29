from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import StudentsForm
from app.models import Students

def index(request):
    return render(request,'app/index.html')

def Users(request):
    form = StudentsForm()

    if request.method=="POST":
        form = StudentsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error from User")
    return render(request,'app/users.html',{'form':form})

def list(request):
    cxt = Students.objects.all()
    context={
        'obj_list': cxt
    }
    return render(request,'app/list.html',context)
