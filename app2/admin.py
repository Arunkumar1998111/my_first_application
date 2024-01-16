from django.contrib import admin
from.models import Userprofile,student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
  list_display = ('name','email','age')

admin.site.register(student, StudentAdmin)
