from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from admininterface.models import *
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
def userhome(request):
    apps=Appcollections.objects.all()
    username = request.session.get('username')
    context={
        'a':apps,
        'n':username
    }

    return render(request,'userhome.html',context=context)

def userregister(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        profile=request.POST.get('Description')
        hashed_password = make_password(password)
        print(name)

        appuser.objects.create(name=name,email=email,username=username,password=hashed_password,profile=profile)
        return redirect('/login')
   

    return render(request,'userregistration.html')



def userlogin(request):
    if request.method=='POST':
        print('enterd')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        print(username)
        user=appuser.objects.filter(username=username).first()
        n=user.username
        print('n',n)
        request.session['username'] = user.username
        print(user)
        if user:
            
            id=user.id
            print('login sucessfull')
            return redirect('/home')
   

    return render(request,'userlogin.html')


def getappdetail(request,id):
    id=id
    username = request.session.get('username')
    app = get_object_or_404(Appcollections, id=id)
    print(app)
    
    return render(request,'appdetail.html',{'a':app,'n':username})


def downloadapp(request,name,points):
    name=name
    id=None
    username = request.session.get('username')
    user=appuser.objects.filter(username=username).first()
    if user:
        print(user)
        id=user.id
 
    points=points
    if request.method=='POST':
        image = request.FILES.get('image')
        Tasks.objects.create(name=name,apppoint=points,image=image,user=user)
        
        context={
        'name':name,
        'points':points
         }
    
        return render(request,'appdownload.html',context=context)
    

def getpoints(request):
    point=0
    username = request.session.get('username')
    user=appuser.objects.filter(username=username).first()
    task=Tasks.objects.filter(user=user)
    for t in task:
        point=point+t.apppoint

    context={
        'n':username,
        'point':point
    }
    return render(request,'userpoints.html',context)

def gettask(request):
    lst=[]
    username = request.session.get('username')
    user=appuser.objects.filter(username=username).first()
    task=Tasks.objects.filter(user=user)
    for t in task:
        lst.append(t.name)
    number=len(lst)
    context={
        'n':username,
        'tasknames':lst,
        'number':number
    }
    return render(request,'usertask.html',context)

def getprofile(request):
    
    username = request.session.get('username')
    user=appuser.objects.filter(username=username).first()
    profile=user.profile
    context={
        'n':username,
        'profile':profile,
       
    }
    return render(request,'userprofile.html',context)


def logout(request):
    request.session.flush()
    
    return redirect('/login')