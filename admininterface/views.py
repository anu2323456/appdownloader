from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import user_passes_test
from userinterface.models import *

def is_admin(user):
    return user.is_authenticated and user.is_staff


def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            print('Login sucessful')
            login(request, user)
            n=user.username
            return redirect('/adminhome',{'n':n})

    return render(request,'adminlogin.html')
    
@user_passes_test(is_admin)
def adminhome(request):
    user=request.user
    appcollections=Appcollections.objects.all()
    task=Tasks.objects.all()
    print(appcollections)
    context={
        'n':user.username,
        'collections':appcollections,
        'task':task
    }
    return render(request,'adminhome.html',context=context)



# Create your views here.
@user_passes_test(is_admin)
def addapp(request):
    user=request.user
    context={
          'n':user.username
        }
    if request.method=='POST':
        name=request.POST.get('name')
        category=request.POST.get('category')
        subcategory=request.POST.get('subcategory')
        link=request.POST.get('link')
        points=request.POST.get('Points')
        image=request.FILES['image']
        Appcollections.objects.create(name=name,category=category,subcategory=subcategory,link=link,points=points,image=image)
        user=request.user
        context={
          'n':user.username
        }
        return redirect('/adminhome',context=context)
    return render(request,'adminadapp.html',context=context)

@user_passes_test(is_admin)
def adminlogout(request):
    user=request.user
    logout(request)
    return redirect('/adminlogin')


@user_passes_test(is_admin)
def deleteapp(request,id):
    appd=Appcollections.objects.filter(id=id).first().delete()
    return redirect('/adminhome')


@user_passes_test(is_admin)
def editapp(request,id):
    app_instance = get_object_or_404(Appcollections, id=id)

    if request.method == 'POST':
        app_instance.name = request.POST.get('name')
        app_instance.category = request.POST.get('category')
        app_instance.subcategory = request.POST.get('subcategory')
        app_instance.link = request.POST.get('link')
        app_instance.points = request.POST.get('Points')
        app_instance.image = request.FILES['image']
        app_instance.save()



        return redirect('/adminhome')
    return render(request,'appedit.html')



