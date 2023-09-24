from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request,'myadmin/index.html',context)

def layout(request):
    context={}
    return render(request,'myadmin/common/layout.html',context)