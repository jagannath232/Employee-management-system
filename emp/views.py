from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'emp/index.html',{'emp_list':emp_list})

def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'emp/insert.html',{'form':form})

def delete_view(request,eno):
    employee = Employee.objects.get(id=eno)
    employee.delete()
    return redirect('/')

def update_view(request,eno):
    employee = Employee.objects.get(eno=eno)
    form = EmployeeForm(instance = employee) #populate form with emp data
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'emp/update.html',{'form':form})
