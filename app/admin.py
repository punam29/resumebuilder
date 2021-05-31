from django.contrib import admin
from app.models import Resume
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display=['summary','name','phoneno','emailid','skills','designation','jobdescription','yearsofexperience'
    ,'schoolname','schoolduration','collegename','collegeduration']

admin.site.register(Resume,ResumeAdmin)
