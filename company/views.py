from django.shortcuts import render,redirect
from company.models import Contact,Register
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
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

def store_contact(request):
    mymessage=request.POST['message']
    myname=request.POST['name']
    myemail=request.POST['email']
    mysubject=request.POST['subject']
    user=request.user.id

    Contact.objects.create(message=mymessage,subject=mysubject,name=myname,email=myemail,user_id=user)
    return redirect('/company/contact')

def common_form(request):
    context={}
    return render(request,'company/common_form.html',context)

def register(request):
    context={}
    return render(request,'company/register.html',context)

def store_register(request):
    myname=request.POST['first_name']
    mylast_name=request.POST['last_name']
    myEMAIL=request.POST['EMAIL']
    mycity=request.POST['city']
    mycountry=request.POST['country']
    myuser_name=request.POST['user_name']
    mypassword=request.POST['password']
    mycpassword=request.POST['cpassword']
    myphoto=request.FILES['photo']

    mylocation=os.path.join(settings.MEDIA_ROOT, 'upload')
    obj=FileSystemStorage(location=mylocation)
    obj.save(myphoto.name,myphoto)

    if mycpassword == mypassword:
        user=User.objects.create_user(first_name=myname,last_name=mylast_name,email=myEMAIL,username=myuser_name,password=mypassword)
        Register.objects.create(city=mycity,country=mycountry,user_id=user.id)
        messages.info(request,"Register Successfully...")
        return redirect('/company/register')
    
    else:
        messages.info(request,"Password Is Not Matching!..")
        return redirect('/company/register')
