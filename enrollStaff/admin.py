from django.contrib import admin
from .models import CreateStaff
# Register your models here.
@admin.register(CreateStaff)
class CreateStaff(admin.ModelAdmin):
    list_display = ('id','name','email','gender','staffType')

