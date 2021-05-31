from django.shortcuts import render

from app.models import Resume
from django.contrib.auth.decorators import login_required


from django.views.generic import DetailView
from easy_pdf.views import PDFTemplateView,PDFTemplateResponseMixin
# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        summary=request.POST.get("summary")
        name=request.POST.get("name")
        phoneno=request.POST.get("phoneno")
        email=request.POST.get("email")
        skills=request.POST.get("skills")
        designation=request.POST.get("designation")
        jobdescription=request.POST.get("jobdescription")
        years=request.POST.get("years")
        schoolname=request.POST.get("schoolname")
        schoolduration=request.POST.get("schoolduration")
        collegename=request.POST.get("collegename")
        collegeduration=request.POST.get("collegeduration")

        resume=Resume(summary=summary,name=name,phoneno=phoneno,
        skills=skills,designation=designation,jobdescription=jobdescription,schoolname=schoolname,
        schoolduration=schoolduration,collegename=collegename,
        collegeduration=collegeduration,emailid=email,yearsofexperience=years)
        resume.save()

    return render(request,"home.html")


def fetchDetails(request,id):
    resume=Resume.objects.get(id=id)
    context={
        'resume':resume
    }
    return render(request,"resume.html",context)




class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Resume
    template_name = 'user_detail.html'


def get_name(request):
    resume=Resume.objects.all()
    context={
        'resume':resume
    }
    return render(request,"myhome.html",context)
    

def nav(request):
    return render(request,"nav.html")

def logout(request):
    return render(request,"logout.html")





