from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'mamatha','age':5}
    return render(request,'data_render.html',context=d)

def data_member(request):
    d={'name':'manoj','age':26,'gender':'male'}
    return render(request,'data_member.html',context=d)