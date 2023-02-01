from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import EmployeeForm
import json
from django.http import JsonResponse
from .models import *

def index(request):
    context = {'users':Employee.objects.all()}
    return render(request, 'index.html', context)


# Create your views here.
def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def return_state_by_country(country):
    
    filepath = './static/data/countries_states.json'
    all_data = readJson(filepath)

    all_states = []

    for x in all_data:
        if x['name'] == country:
            if 'states' in x:
                for state in x['states']:
                    y = (state['name'], state['name'])
                    all_states.append(state['name'])
            else:
                all_states.append(country)

    return all_states

def getProvince(request):
    country = request.POST.get('country', None)
    provinces = return_state_by_country(country)
    return JsonResponse({'provinces': provinces})



def employers_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.state = request.POST.get('state')
            employee.photo=request.FILES.get('photo')
            employee.save()

            messages.success(request, f'Employee form created sucessfully')    
            return redirect('index')
    else:
        form = EmployeeForm()

    context= {'form':form}
    return render(request, 'employers_form.html', context)

def editEmployee(request,id):
    user = Employee.objects.get(id=id)
    initial_dict = {
        "state" : user.state,
    }
    EditForm = EmployeeForm(instance=user, initial = initial_dict)
    if request.method == 'POST':
        EditForm = EmployeeForm(request.POST, instance=user, initial = initial_dict)
        if EditForm.is_valid():
            employee = EditForm.save(commit=False)
            employee.state = request.POST.get('state')
            
            if request.FILES.get('photo') !=  None:
                employee.photo=request.FILES.get('photo')
            employee.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('index')
    return render(request, 'edit_Employee.html', {'user': user, 'form': EditForm})


def deleteEmployee(request):
    employee_id = request.GET.get('id', None)
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    data = {
        'deleted': True
    }
    messages.success(request, 'Employee deteted successfully.')
    return JsonResponse(data)