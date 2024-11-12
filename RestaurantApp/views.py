from django.shortcuts import render, redirect
from RestaurantApp.models import CatDB, FoodDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(req):
    return render(req, "index.html")
def AddCat(req):
    return render(req, "AddCat.html")
def SaveCat(req):
    if req.method=="POST":
        a = req.POST.get('catname')
        b = req.POST.get('des')
        c = req.FILES['image']
        obj = CatDB(CatName=a, Description=b, Image=c)
        obj.save()
        return redirect(AddCat)
def ViewCat(req):
    data = CatDB.objects.all()
    return render(req, "ViewCat.html", {'data': data})
def deleteCat(req,cat_id):
    a = CatDB.objects.filter(id=cat_id)
    a.delete()
    return redirect(ViewCat)
def editCat(req,cat_id):
    data = CatDB.objects.get(id=cat_id)
    return render(req,"editCat.html" ,{'data':data})
def updateCat(req,cat_id):
    if req.method == "POST":
        a = req.POST.get('catname')
        b = req.POST.get('des')
        c = req.FILES['image']
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CatDB.objects.get(id=cat_id).Image
        CatDB.objects.filter(id=cat_id).update(CatName=a, Description=b, Image= c)
        return redirect(ViewCat)




def AddFood(req):
    CatName = CatDB.objects.all()
    return render(req, "AddFood.html", {"CatName":CatName})
def SaveFood(req):
    if req.method=="POST":
        a = req.POST.get('catname')
        b = req.POST.get('fname')
        c = req.POST.get('des')
        d = req.POST.get('price')
        e = req.FILES['image']
        obj = FoodDB(CatName=a,FoodName=b, Description=c, Price=d, Image=e,)
        obj.save()
        return redirect(AddFood)
def ViewFood(req):
    data = FoodDB.objects.all()
    return render(req, "ViewFood.html", {'data': data})
def editFood(req,f_id):
    cat = CatDB.objects.all()
    data = FoodDB.objects.get(id=f_id)
    return render(req,"editFood.html" ,{'data':data, 'cat':cat})
def updateFood(req,f_id):
    if req.method == "POST":
        a = req.POST.get('catname')
        b = req.POST.get('fname')
        c = req.POST.get('des')
        d = req.POST.get('price')
        e = req.FILES['image']
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = FoodDB.objects.get(id=f_id).Image
        FoodDB.objects.filter(id=f_id).update(CatName=a,FoodName=b, Description=c, Price=d, Image=e)
        return redirect(ViewFood)
def deleteFood(req,f_id):
    a = FoodDB.objects.filter(id=f_id)
    a.delete()
    return redirect(ViewFood)

def AdminLogin(request):
    return render(request, "AdminLogin.html")
def Admin_login(request):
    if request.method =="POST":
        a=request.POST.get('username')
        b=request.POST.get('password')
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a, password=b)
            if x is not None:
                login(request,x)
                return redirect(index)
            else:
                return redirect(AdminLogin)