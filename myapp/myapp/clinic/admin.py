from django.contrib import admin
from clinic.models import *
# Register your models here.
#class DoctorAdmin(admin.ModelAdmin):
#    list_display = ['Name_EN' , 'Name_AR' , 'Image']
#admin.site.register(Doctor , DoctorAdmin)
class aboutAdmin(admin.ModelAdmin):
    list_display = ['about_title_en' , 'about_title_ar' , 'image_name']
admin.site.register(about , aboutAdmin)
class appointmentsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'phone' , 'mail']
admin.site.register(appointments,appointmentsAdmin)
class branchesAdmin(admin.ModelAdmin):
    list_display = ['branch_name_en' , 'branch_name_ar' , 'mail']
admin.site.register(branches,branchesAdmin)
class galleryAdmin(admin.ModelAdmin):
    list_display = ['photo' , 'video']
admin.site.register(gallery,galleryAdmin)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['title_en' , 'title_ar' , 'logo_name']
admin.site.register(Info,InfoAdmin)
class personsAdmin(admin.ModelAdmin):
    list_display = ['person_name_en' , 'person_name_ar' , 'person_phone' , 'person_mail']
admin.site.register(persons,personsAdmin)
class servicesAdmin(admin.ModelAdmin):
    list_display = ['service_name_en' , 'service_name_ar' , 'image_name']
admin.site.register(services,servicesAdmin)
class sliderAdmin(admin.ModelAdmin):
    list_display = ['image_name' , 'orders']
admin.site.register(slider,sliderAdmin)
class statisticsAdmin(admin.ModelAdmin):
    list_display = ['number','name_en' , 'name_ar']
admin.site.register(statistics,statisticsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['abstract','caption']
admin.site.register(post,PostAdmin)