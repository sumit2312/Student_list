from django.shortcuts import render,get_object_or_404,redirect
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

def dynamic_view(request, id):
    # obj = Students.objects.get(id=id)
    obj = get_object_or_404(Students,id=id)
    context={
        "object":obj
    }
    return render(request,'app/student_detail.html',context)

def student_delete(request, id):
    obj = get_object_or_404(Students,id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('../../')
    context={
        "object":obj
    }
    return render(request,'app/student_delete.html',context)