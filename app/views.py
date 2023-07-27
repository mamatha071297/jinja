from django.shortcuts import render

# Create your views here.

def data_member(request):
    d={'name':'manoj','age':26,'gender':'male'}
    return render(request,'data_member.html',context=d)