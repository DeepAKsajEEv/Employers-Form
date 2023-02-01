from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('employers-form', employers_form, name='employers-form'),
    path('get-province',getProvince, name='get-province'),
    path('employee-edit/<int:id>',editEmployee, name='edit-employee'),
    path('delete',deleteEmployee, name='delete-employee'),

]
