from django.contrib import admin
from .models import ServiceUpdate,User,ServiceRequest,Category

@admin.register(ServiceUpdate)
class ServiceUpdateAdmin(admin.ModelAdmin):
    list_display=('id','servicerequest','description','created_at')

# Register your models here.
