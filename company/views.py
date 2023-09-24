from django.shortcuts import render

# Create your views here.
def layout(request):
    context={}
    return render(request,'company/common/layout.html',context)