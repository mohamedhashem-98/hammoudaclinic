from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from django.core.mail import send_mail
import datetime
# Create your views here.
def index(request):
    slider = models.slider.objects.all().order_by('orders')
    statitistics = models.statistics.objects.all()
    about = models.about.objects.all()
    person = models.persons.objects.all()
    galleryphoto = models.gallery.objects.filter(photo__isnull=False)[:3]
    galleryvideo = models.gallery.objects.filter(video__isnull=False)[:3]
    branches = models.branches.objects.all()
    services = models.services.objects.all()
    time = models.branches.objects.values('time_table_en')
    post = models.post.objects.all().order_by('-id')[:6]
    Info = models.Info.objects.all()
    if len(time) > 0:
        if time[0]['time_table_en']:
             time = time[0]['time_table_en'].split(',')
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.appointments(name=name , phone=phone , mail=email , message=message , reservation_date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'Hammouda Clinic',
            name + " , Has Booked With HammoudaClinic , and He Wait Your Reply To Confirm His Booking By Phone: " + phone + "  Or Mail:" + email + " \n And His Message Was " + message + " \n Thanks For Your Interest With Your Patients , and Nice Day For You Dr. Ahmed Ismail Hammouda :D . ",
            email,
            ['info@hammoudaclinic.com' , 'hashim@algawhar.com'],
            fail_silently=False,
        )
        send_mail(
            'Hammouda Clinic',
           "Dear: " + name + " , you Already Booked With HammoudaClinic \n Thanks For Choosing Us And Your Doctor Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name ,
            'info@hammoudaclinic.com',
            [email],
            fail_silently=False,
        )
        return redirect('reserve')

    return render(request ,"static_pages/index.html" , {'slider':slider , 'statitistics' : statitistics , 'about':about , 'person':person , 'photo':galleryphoto , 'video':galleryvideo , 'branches':branches , 'services':services , 'time':time , 'posts':post , 'info':Info})
def reserve(request):
    return redirect('index')
def reservear(request):
    return redirect('ar')
def gallery(request):
    galleryphoto = models.gallery.objects.filter(photo__isnull=False)
    galleryvideo = models.gallery.objects.filter(video__isnull=False)
    branches = models.branches.objects.all()
    about = models.about.objects.all()
    time = models.branches.objects.values('time_table_en')
    Info = models.Info.objects.all()
    if len(time) > 0:
        if time[0]['time_table_en'] :
            time = time[0]['time_table_en'].split(',')
    return render(request , 'static_pages/gallery.html' ,{'photo' : galleryphoto , 'video' :galleryvideo , 'about':about ,
                                             'branches':branches , 'time':time , 'info':Info})
def galleryar(request):
    galleryphoto = models.gallery.objects.filter(photo__isnull=False)
    galleryvideo = models.gallery.objects.filter(video__isnull=False)
    branches = models.branches.objects.all()
    about = models.about.objects.all()
    time = models.branches.objects.values('time_table_ar')
    Info = models.Info.objects.all()
    if len(time) > 0:
        if time[0]['time_table_ar']:
            time = time[0]['time_table_ar'].split(',')
    return render(request , 'static_pages/galleryar.html' ,{'photo' : galleryphoto , 'video' :galleryvideo , 'about':about ,
                                             'branches':branches , 'time':time , 'info':Info})
def ar(request):
    slider = models.slider.objects.all().order_by('orders')
    statitistics = models.statistics.objects.all()
    about = models.about.objects.all()
    person = models.persons.objects.all()
    galleryphoto = models.gallery.objects.filter(photo__isnull=False)[:3]
    galleryvideo = models.gallery.objects.filter(video__isnull=False)[:3]
    branches = models.branches.objects.all()
    services = models.services.objects.all()
    time = models.branches.objects.values('time_table_ar')
    post = models.post.objects.all().order_by('-id')[:6]
    Info = models.Info.objects.all()
    if len(time) > 0:
        if time[0]['time_table_ar']:
            time = time[0]['time_table_ar'].split(',')
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        tmp = models.appointments(name=name, phone=phone, mail=email, message=message,
                                  reservation_date=datetime.datetime.now())
        tmp.save()
        send_mail(
            'Hammouda Clinic',
            name + " , Has Booked With HammoudaClinic , and He Wait Your Reply To Confirm His Booking By Phone: " + phone + "  Or Mail:" + email + " \n And His Message Was " + message + " \n Thanks For Your Interest With Your Patients , and Nice Day For You Dr. Ahmed Ismail Hammouda :D . ",
            email,
            ['info@hammoudaclinic.com' , 'hashim@algawhar.com'],
            fail_silently=False,
        )
        send_mail(
            'Hammouda Clinic',
           "Dear: " + name + " , you Already Booked With HammoudaClinic \n Thanks For Choosing Us And Your Doctor Will Contact With You By Phone Or E-Mail Soon \n Thanks For You Mr/Mrs: " + name ,
            'info@hammoudaclinic.com',
            [email],
            fail_silently=False,
        )
        return redirect('reservear')

    return render(request, "static_pages/arabic.html",
                  {'slider': slider, 'statitistics': statitistics, 'about': about, 'person': person,
                   'photo': galleryphoto, 'video': galleryvideo, 'branches': branches, 'services': services,
                   'time': time , 'posts':post , 'info':Info})
                   
def services(request , id):
    serv = models.services.objects.filter(id = id)
    Info = models.Info.objects.all()
    return render(request  , 'static_pages/services.html' , {'reqserv' : serv , 'info':Info})

def servicesar(request , id):
    serv = models.services.objects.filter(id = id)
    Info = models.Info.objects.all()
    return render(request  , 'static_pages/servicesar.html' , {'reqserv' : serv , 'info':Info})
    
def posts(request , id):
        post = models.post.objects.filter(id = id)
        Info = models.Info.objects.all()
        return render(request  , 'static_pages/posts.html' , {'reqpost':post , 'op':0 , 'info':Info})
        
def postsN(request ):
        post = models.post.objects.all().order_by('-id')
        Info = models.Info.objects.all()
        return render(request  , 'static_pages/posts.html' , {'reqpost':post , 'op':1 , 'info':Info})
        
        
def postsar(request , id):
        post = models.post.objects.filter(id = id)
        Info = models.Info.objects.all()
        return render(request  , 'static_pages/postsar.html' , {'reqpost':post , 'op':0 , 'info':Info})
        
def postsNar(request ):
        post = models.post.objects.all().order_by('-id')
        Info = models.Info.objects.all()
        return render(request  , 'static_pages/postsar.html' , {'reqpost':post , 'op':1 , 'info':Info})
    
    
