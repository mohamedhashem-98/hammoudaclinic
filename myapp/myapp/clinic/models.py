from django.db import models
#from django_mysql.models import ListTextField
#from ckeditor.fields import RichTextField
# Create your models here.
class about(models.Model):
    about_title_en = models.TextField(blank=True , null=True)
    about_title_ar = models.TextField(blank=True, null=True)
    about_short_desc_en = models.TextField(blank=True , null=True)
    about_short_desc_ar = models.TextField(blank=True , null= True)
    about_long_desc_en = models.TextField(blank=True , null=True)
    about_long_desc_ar = models.TextField(blank=True , null=True)
    image_name = models.ImageField(upload_to='photo/' , blank=True , null=True)

class appointments(models.Model):
    name = models.CharField(max_length=150 , null=True , blank=True)
    phone = models.CharField(max_length=15 , null=True , blank= True)
    mail = models.EmailField(null=True , blank=True)
    message = models.TextField(null=True , blank=True)
    reservation_date = models.DateTimeField(blank=True , null=True)

class branches(models.Model):
    branch_name_en = models.CharField(max_length=255, null=True , blank=True)
    branch_name_ar = models.CharField(max_length=255, null=True, blank=True)
    address_en = models.CharField(max_length=255, null=True, blank=True)
    address_ar = models.CharField(max_length=255, null=True, blank=True)
    location = models.TextField(null=True , blank=True)
    phone = models.CharField(max_length=255, null=True , blank=True)
    mail = models.EmailField(null=True , blank=True)
    time_table_en = models.TextField(null=True , blank=True)
    time_table_ar = models.TextField(null=True, blank=True)
    Facebook = models.CharField(max_length=255, null=True , blank=True)
    Instgram = models.CharField(max_length=255, null=True, blank=True)
    Youtube = models.CharField(max_length=255, null=True, blank=True)
    GoogleBussiness = models.CharField(max_length=255, null=True, blank=True)

class gallery(models.Model):
    photo = models.ImageField(upload_to='photo/' , blank=True , null=True)
    video = models.CharField( max_length=255 , blank=True , null=True)

class Info(models.Model):
    title_en = models.CharField(max_length=255, null=True , blank=True)
    title_ar = models.CharField(max_length=255, null=True, blank=True)
    desc_en = models.CharField(max_length=255, null=True, blank=True)
    desc_ar = models.CharField(max_length=255, null=True, blank=True)
    keywords_en = models.TextField(null=True , blank=True)
    keywords_ar = models.TextField(null=True, blank=True)
    logo_name = models.ImageField(upload_to='photo/' , blank=True , null=True)
    icon_name = models.ImageField(upload_to='photo/', blank=True, null=True)

class persons(models.Model):
    person_name_en = models.CharField(max_length=150 , blank=True , null=True)
    person_name_ar = models.CharField(max_length=150, blank=True, null=True)
    person_job_en = models.CharField(max_length=255, blank=True, null=True)
    person_job_ar = models.CharField(max_length=255, blank=True, null=True)
    person_short_desc_en = models.TextField(null=True , blank=True)
    person_short_desc_ar = models.TextField(null=True, blank=True)
    person_long_desc_en = models.TextField(null=True , blank=True)
    person_long_desc_ar = models.TextField(null=True, blank=True)
    person_keywords_en = models.TextField(null=True, blank=True)
    person_keywords_ar = models.TextField(null=True, blank=True)
    person_phone = models.CharField(max_length=150, blank=True, null=True)
    person_mail = models.EmailField(null=True, blank=True)
    person_birth_date = models.DateField(null=True, blank=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    cv_en = models.TextField(null=True, blank=True)
    cv_ar = models.TextField(null=True, blank=True)
    image_name = models.ImageField(upload_to='photo/', blank=True, null=True)

class services(models.Model):
    parent_id = models.CharField(max_length=6 , null=True, blank=True)
    service_name_en = models.CharField(max_length=255, blank=True, null=True)
    service_name_ar = models.CharField(max_length=255, blank=True, null=True)
    short_desc_en = models.TextField(null=True, blank=True)
    short_desc_ar = models.TextField(null=True, blank=True)
    keywords_en =  models.TextField(null=True, blank=True)
    keywords_ar = models.TextField(null=True, blank=True)
    long_desc_en = models.TextField(null=True, blank=True)
    long_desc_ar = models.TextField(null=True, blank=True)
    image_name = models.ImageField(upload_to='photo/', blank=True, null=True)
    orders = models.IntegerField(null=True, blank=True)

class slider(models.Model):
    desc_en = models.TextField(null=True, blank=True)
    desc_ar = models.TextField(null=True, blank=True)
    image_name = models.ImageField(upload_to='photo/', blank=True, null=True)
    orders = models.IntegerField(null=True, blank=True)

class statistics(models.Model):
    number = models.IntegerField(null=True, blank=True)
    name_en = models.CharField(max_length=150, blank=True, null=True)
    name_ar = models.CharField(max_length=150, blank=True, null=True)
    image_name = models.ImageField(upload_to='photo/', blank=True, null=True)
    description_en = models.TextField(null=True, blank=True)
    description_ar = models.TextField(null=True, blank=True)
    
    
class post(models.Model):
    caption = models.CharField(max_length = 150 , blank = True , null = True)
    abstract = models.TextField(blank = True , null = True)
    text = models.TextField(blank = True , null = True)
    image = models.ImageField(upload_to='photo/' , null = True , blank = False)
    video = models.FileField(upload_to ='video/' , blank = True , null = True)
    





















