from django.shortcuts import render,redirect
from Backend.models import CarDb
from django.db.models import Q
from Frontend.models import RegistrationDb,ContactDb,EnquiryDb,Review,Profile,PaymentDb
from Frontend.forms import CreateUserform
from Frontend.forms import CreateUserform,CarPaymentForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from CarDealerProject.settings import EMAIL_HOST_USER
from django.contrib import messages
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseBadRequest
from Frontend.help import send_forgot_pass
from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
import uuid
from CarDealerProject import settings
from CarDealerProject.settings import STATIC_URL
from django.template.loader import get_template
import os
from xhtml2pdf import pisa
from rest_framework.views import View
import razorpay
# Create your views here.

def home_page(request):
    car = CarDb.objects.all()
    return render(request,"home.html",{'car':car})

def car_details(request,d_id):
    data = CarDb.objects.get(id=d_id)
    return render(request,"car_details.html",{'data':data})

def all_cars(request):
    car = CarDb.objects.all()
    return render(request,"all_cars.html",{'car':car})

def login_user(request):
    return render(request,"login.html")

def register_user(request):
    return render(request,"signup_user.html")

def search_car(request):
   if request.method=="POST":
       searched = request.POST['searched']
       multiple = Q(Q(Name__contains=searched) | Q(Model__contains=searched)
                    | Q(Engine__contains=searched) | Q(Body_Style__contains=searched) | Q(Type__contains=searched))
       Cars = CarDb.objects.filter(multiple)
       return render(request,"search_car.html",{'searched':searched,'Cars':Cars})
   else:
       return render(request, "search_car.html")

def save_registration(request):
    if request.method=="POST":
        fna = request.POST.get('fname')
        lna = request.POST.get('lname')
        em = request.POST.get('email')
        usn = request.POST.get('uname')
        psw = request.POST.get('password')
        obj = RegistrationDb(FirstName=fna,LastName=lna,Email=em,Username=usn,Password=psw)
        obj.save()
        return redirect(register_user)

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            messages.success(request,"Welcome")
            login(request, user)
            return redirect(home_page)
        else:
            messages.warning(request, "Invalid Username or Password...")
            return redirect(login_user)

    return render(request,"login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "logged out successfully....")
    return redirect(login_user)

def signup_view(request):
    form = CreateUserform()
    if request.method=="POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form = CreateUserform(request.POST)

        if User.objects.filter(email=email).exists():
            messages.warning(request,"email already exist...")
            return redirect(user_login)
        elif form.is_valid():

            # form.save()
            # print("form saved")
            otp = random.randint(100000, 999999)
            send_mail("User Data:",f"Verify your mail by the the OTP:  {otp}",EMAIL_HOST_USER,[email],fail_silently=True)
            messages.success(request, "Registration Done... You can login now")
            return render(request,"verify.html",{'otp': otp,'first_name':first_name,'last_name':last_name,'email':email,'username':username,'password1':password1,'password2':password2})
        else:
            print("form error:",form.errors)
            messages.warning(request, "Registration Failed...")
    context = {'form':form}
    return render(request,"signup.html",context)

@csrf_exempt
def VerifyOtp(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save()

        print("OTP: ",userotp)
    return JsonResponse({'data': 'data'},status=200)

def account_created(request):
    return render(request,"account.html")

def about_page(request):
    return render(request,"about.html")

def teams(request):
    return render(request,"teams.html")

def blog(request):
    return render(request,"blog.html")

def testimonials(request):
    review = Review.objects.all()
    return render(request,"testimonials.html",{'review':review})

def faq(request):
    return render(request,"faq.html")


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        obj = ContactDb(Name=name,Email=email,Subject=subject,Message=message)
        obj.save()

        send_mail(
            email,
            message,
            email, #from email
            ['cardealer877@gmail.com'] #to email
        )
        return render(request,'contact.html',{'name':name,'email':email,'subject':subject,'message':message})
    else:
        return render(request,'contact.html')

def Enquiry(request,d_id):
    if request.method=="POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        carname = request.POST.get('carname')
        offer = request.POST.get('offer')
        description = request.POST.get('description')
        car_id = request.POST.get('car_id')
        data = CarDb.objects.get(id=d_id)
        price = request.POST.get('price')
        obj = EnquiryDb(Name=name,Email=email,Mobile=mobile,Car_Name=carname,Offer=offer,Description=description,Username=username,Car_Id=car_id,Price=price)
        obj.save()
        messages.success(request, "Your Enquiry has been sent...")
        return render(request,'car_details.html',{'data':data})

def enquiry_page(request):
    data = EnquiryDb.objects.filter(Username=request.user)
    return render(request,"enquiries.html",{'data':data})

def pay_details(reqeust,p_id):
    pay = PaymentDb.objects.get(id=p_id)
    return render(reqeust,"enquires.html",{'pay':pay})


def delete_inq(request,d_id):
    data = EnquiryDb.objects.filter(id=d_id)
    data.delete()
    return redirect(enquiry_page)


def save_review(request):
    if request.method=="POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating3')
        message = request.POST.get('message')
        obj = Review(Stars=rating,Message=message,Username=name)
        obj.save()
        messages.success(request, "Thanks for your review...")
        return redirect(home_page)

def review_page(request):
    return render(request, "review.html")

def make_payment(request,e_id):
    if request.method=="POST":
        name = request.POST.get('name')
        carname = request.POST.get('carname')
        carid = request.POST.get('carid')
        amount = int(request.POST.get('amount'))

        client = razorpay.Client(auth=("key","secretkey"))

        response_payment = client.order.create(dict(amount=amount*100,currency='INR'))

        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            pay = PaymentDb(name=name,car_name=carname,car_id=carid,amount=amount,order_id=order_id)
            pay.save()

            response_payment['name']=name

            form = CarPaymentForm(request.POST or None)
            return render(request,"carpay.html",{'form':form,'payment':response_payment})

    form = CarPaymentForm()
    data = EnquiryDb.objects.get(id=e_id)
    return render(request,"carpay.html",{'data':data,'form':form})

@csrf_exempt
def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    client = razorpay.Client(auth=('rzp_test_3qlipsZGG6ZBBc', '66Z2B6dHsrVUOp8jn5l9UgE7'))
    try:

        status = client.utility.verify_payment_signature(params_dict)
        print(status)
        pay = PaymentDb.objects.get(order_id=response['razorpay_order_id'])
        pay.razorpay_payment_id = response['razorpay_payment_id']
        pay.paid = True
        pay.save()
        if status is not None:
            template = get_template('invoice.html')
            data = {
                'order_id': pay.order_id,
                'transaction_id': pay.razorpay_payment_id,
                'name': pay.name,
                'car_name': pay.car_name,
                'amount': pay.amount,
                'payment': pay
            }
            html = template.render(data)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
            pdf = result.getvalue()
            filename = 'Invoice_' + data['order_id'] + '.pdf'

            mail_subject = 'Recent Order Details'
            # message = render_to_string('firstapp/payment/emailinvoice.html', {
            #     'user': order_db.user,
            #     'order': order_db
            # })
            # context_dict = {
            #     'user': order_db.user,
            #     'order': order_db
            # }
            # template = get_template('firstapp/payment/emailinvoice.html')
            # message = template.render(context_dict)
            # to_email = order_db.user.email
            # email = EmailMessage(
            #     mail_subject,
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     [to_email]
            # )

            # for including css(only inline css works) in mail and remove autoescape off
            # email = EmailMultiAlternatives(
            #     mail_subject,
            #     "hello",  # necessary to pass some message here
            #     settings.EMAIL_HOST_USER,
            #     [to_email]
            # )
            # email.attach_alternative(message, "text/html")
            # email.attach(filename, pdf, 'application/pdf')
            # email.send(fail_silently=False)
            return render(request,"pay_success.html", {'id': pay.id})
        else:
            return render(request,"pay_fail.html")
    except:
        return render(request,"pay_fail.html")
@csrf_exempt
def pay_success(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id','')
            razorpay_order_id = request.POST.get('razorpay_order_id','')
            razorpay_signature = request.POST.get('razorpay_signature','')
            params_dict = {
                'razorpay_order_id':razorpay_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':razorpay_signature
            }
            client = razorpay.Client(auth=('rzp_test_3qlipsZGG6ZBBc', '66Z2B6dHsrVUOp8jn5l9UgE7'))
            payment = PaymentDb.objects.get(order_id=razorpay_order_id)
            payment.razorpay_payment_id = payment_id
            payment.paid = True
            payment.save()

            #for invoice pdf

            status = client.utility.verify_payment_signature(params_dict)
            print(status)
            if status is not None:
                print(razorpay_order_id)
                try:
                    template = get_template('invoice.html')
                    data = {
                        'order_id': payment.order_id,
                        'transaction_id': payment.razorpay_payment_id,
                        'amount': payment.amount
                    }
                    html = template.render(data)
                    result = BytesIO()
                    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),
                                            result)  # , link_callback=fetch_resources)
                    pdf = result.getvalue()
                    filename = 'Invoice_' + data['order_id'] + '.pdf'

                    mail_subject = 'Recent Order Details'
                    # message = render_to_string('firstapp/payment/emailinvoice.html', {
                    #     'user': order_db.user,
                    #     'order': order_db
                    # })
                    # context_dict = {
                    #     'user': order_db.user,
                    #     'order': order_db
                    # }
                    # template = get_template('firstapp/payment/emailinvoice.html')
                    # message = template.render(context_dict)
                    # to_email = order_db.user.email
                    # email = EmailMessage(
                    #     mail_subject,
                    #     message,
                    #     settings.EMAIL_HOST_USER,
                    #     [to_email]
                    # )

                    # for including css(only inline css works) in mail and remove autoescape off
                    # email = EmailMultiAlternatives(
                    #     mail_subject,
                    #     "hello",  # necessary to pass some message here
                    #     settings.EMAIL_HOST_USER,
                    #     [to_email]
                    # )
                    # email.attach_alternative(message, "text/html")
                    # email.attach(filename, pdf, 'application/pdf')
                    # email.send(fail_silently=False)

                    client.payment.capture(payment_id)
                    payment.status = True
                    payment.save()
                    return render(request,"pay_success.html",{'id':payment.id})
                except:
                    return render(request,"pay_success.html",{'id':payment.id})
            else:
                return render(request, "pay_fail.html")
        except:
            return render(request, "pay_fail.html")
    else:
        return render(request,"pay_fail.html")


def chatbot(request):
    return render(request,"chatbot.html")

def fetch_resources(uri,rel):
    path = os.path.join(uri.replace(settings.STATIC_URL,""))
    return path
def render_to_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

def payment_pdf(request):

    return render(request,"receipt.html")

class GenerateInvoice(View):
    def get(self,request,pk,*args,**kwargs):
        try:
            payment = PaymentDb.objects.get(id=pk,paid=True)
        except:
            return HttpResponse("505 Not found...")
        data = {
            'order_id':payment.order_id,
            'transaction_id':payment.razorpay_payment_id,
            'name':payment.name,
            'car_name':payment.car_name,
            'amount':payment.amount,
            'payment':payment
        }
        pdf = render_to_pdf('receipt.html',data)
        if pdf:
            response = HttpResponse(pdf,content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(data['order_id'])
            content = "Inline; filename='%s'" %(filename)
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Not found")

def change_pass(request):
    form = CreateUserform()
    return render(request,"change_pass.html",{'form':form})