from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to the project</h1>')

def home(request):
    return HttpResponse('<h1>Welcome to the Home</h1>')

def hainame(request,name):
    return HttpResponse('<h2>hello {}</h2>'.format(name))

def add(request, a, b):
    return HttpResponse("<h1> the sum of {} and {} = {}</h1>".format(a,b,int(a)+int(b)))

def tempdemo(request):
    fruits=['apple','mango', 'guava','chikk']
    return render(request,'template.html',context={'name':'akash','fruits':fruits})


def grt2(request,a,b):
    return render(request,'template2.html',context={'a':a,'b':b})

def indextax(request):
    return render(request,'indextax.html')

def hometemp(request):
    return render(request,'pages/home.html')

def abouttemp(request):
    return render(request,'pages/about.html')

def registertemp(request):
    if request.method=="POST":
        name=request.POST.get("fname")
        lname=request.POST.get("lname")
        file=None
        if request.FILES:
            file= request.FILES['profilepic']
            fs=FileSystemStorage()
            savedfile=fs.save(file.name,file)
            file_url=fs.url(savedfile)

        return HttpResponse("<h1>Form submitted successfully {} <br> verify the details <br> name: {} <br> email: {} <br> profilepic :<img src='{}'> ".format(name,name,lname,file_url))

    return render(request,'pages/register.html')