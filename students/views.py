from django.shortcuts import render,redirect
from .forms import StudentForm

from .models import Student

def home(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'students/dashboard.html',context)

def create(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            return redirect('home')
    else:
        form = StudentForm()
    
    return render(request,'students/create-student.html',{'form':form})


def update(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            form = StudentForm()
            return redirect('home')
            
        
        

    return render(request, 'students/update-student.html',{'form':form})


def delete(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request,'students/delete.html',{'student':student})