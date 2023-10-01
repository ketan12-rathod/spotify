from django.shortcuts import render

# Create your views here.
def layout(request):
    context={}
    return render(request,'company/common/layout.html',context)

def index(request):
    context={}
    return render(request,'company/index.html',context)

def contact(request):
    context={}
    return render(request,'company/contact.html',context)