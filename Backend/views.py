from django.shortcuts import render,redirect
from Backend.models import CarDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Frontend.models import EnquiryDb,PaymentDb
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index_page(request):
    return render(request,"index.html")

def add_car(request):
    return render(request,"add_car.html")

def save_car(request):
    if request.method=="POST":
        cna = request.POST.get('name')
        mod = request.POST.get('model')
        des = request.POST.get('description')
        img1 = request.FILES['image-1']
        img2 = request.FILES['image-2']
        img3 = request.FILES['image-3']
        img4 = request.FILES['image-4']
        pri = request.POST.get('price')
        mil = request.POST.get('mileage')
        eng = request.POST.get('engine')
        trn = request.POST.get('transmission')
        ful = request.POST.get('fuel')
        sea = request.POST.get('seat')
        col = request.POST.get('color')
        dor = request.POST.get('door')
        yea = request.POST.get('year')
        pow = request.POST.get('power')
        sty = request.POST.get('bodystyle')
        typ = request.POST.get('type')
        fea = request.POST.get('features')
        obj = CarDb(Name=cna,Model=mod,Description=des,Image_1=img1,Image_2=img2,Image_3=img3,Image_4=img4,Price=pri,
            Mileage=mil,Engine=eng,Transmission=trn,Fuel_Type=ful,Seats=sea,Color=col,Doors=dor,Year=yea,Power=pow,Body_Style=sty,Type=typ,Features=fea)
        obj.save()
        messages.success(request,"Car Added Successfully...")
        return redirect(add_car)

def display_car(request):
    data = CarDb.objects.all()
    return render(request,"display_car.html",{'data':data})

def enquiry_page_backend(request):
    data = EnquiryDb.objects.all()
    return render(request,"enquiry_bknd.html",{'data':data})

def edit_car(request,c_id):
    car = CarDb.objects.get(id=c_id)
    return render(request,"edit_car.html",{'car':car})

def update_car(request,c_id):
    if request.method=="POST":
        cna = request.POST.get('name')
        mod = request.POST.get('model')
        des = request.POST.get('description')
        try:
            img1 = request.FILES['image-1']
            fs = FileSystemStorage()
            file_1 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file_1 = CarDb.objects.get(id=c_id).Image_1
        try:
            img2 = request.FILES['image-2']
            fs = FileSystemStorage()
            file_2 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file_2 = CarDb.objects.get(id=c_id).Image_2
        try:
            img3 = request.FILES['image-3']
            fs = FileSystemStorage()
            file_3 = fs.save(img3.name,img3)
        except MultiValueDictKeyError:
            file_3 = CarDb.objects.get(id=c_id).Image_3
        try:
            img4 = request.FILES['image-4']
            fs = FileSystemStorage()
            file_4 = fs.save(img4.name,img4)
        except MultiValueDictKeyError:
            file_4 = CarDb.objects.get(id=c_id).Image_4
        pri = request.POST.get('price')
        mil = request.POST.get('mileage')
        eng = request.POST.get('engine')
        trn = request.POST.get('transmission')
        ful = request.POST.get('fuel')
        sea = request.POST.get('seat')
        col = request.POST.get('color')
        dor = request.POST.get('door')
        yea = request.POST.get('year')
        pow = request.POST.get('power')
        sty = request.POST.get('bodystyle')
        typ = request.POST.get('type')
        fea = request.POST.get('features')
        obj = CarDb.objects.filter(id=c_id).update(Name=cna, Model=mod, Description=des, Image_1=file_1, Image_2=file_2, Image_3=file_3, Image_4=file_4,
                    Price=pri,
                    Mileage=mil, Engine=eng, Transmission=trn, Fuel_Type=ful, Seats=sea, Color=col, Doors=dor, Year=yea,
                    Power=pow, Body_Style=sty, Type=typ, Features=fea)

        messages.success(request,"Car updated successfully...")
        return redirect(display_car)

def delete_car(request,c_id):
    data = CarDb.objects.filter(id=c_id)
    data.delete()
    messages.success(request,"Car deleted Successfully...")
    return redirect(display_car)

def login_page(request):
    return render(request,"login_page.html")

def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('uname')
        psw = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=psw)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = psw
                messages.success(request,"welcome...")
                return redirect(index_page)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logged out Successfully...")
    return redirect(login_page)

def enq_approve(request,enq_id):
    enquiry = EnquiryDb.objects.get(id=enq_id)
    enquiry.Status = 1
    enquiry.save()
    return redirect(enquiry_page_backend)

def enq_reject(request,enq_id):
    enquiry = EnquiryDb.objects.get(id=enq_id)
    enquiry.Status = 2
    enquiry.save()
    return redirect(enquiry_page_backend)

def payment_details(request):
    data = PaymentDb.objects.all()
    return render(request,"payment_details.html",{'data':data})