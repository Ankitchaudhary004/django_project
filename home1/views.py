

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .models import iceCream,carousel
from .models import Contact,about
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# context={
#     "variable1":"Using django is good "
# }
# def index(request):
#     return render(request,'index.html',context)
#     #return HttpResponse("this is homepage")

def  yt(request):
    return render(request,'yyyt.html',)
    #return HttpResponse("this is about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")
def contact(request):
   return render(request,'contact.html')
    #return HttpResponse("this is contact page")

def showView(request):
    obj = iceCream.objects.all()
    carousels = carousel.objects.all()
    template_name = 'index.html'
    context = {'obj': obj, 'carouselObj': carousels}
    return render(request, template_name, context)


def showAbout(request):
    aboutObj = about.objects.all()
    template_name = 'about.html'
    context = {'aboutObj':aboutObj}
    return render(request, template_name, context)


# def contact(request):
#     if request.method=="POST":
#      contact=contact(request)
#      first_name= request.POST.get('fname')
#      last_name= request.POST.get('lname')
#      country= request.POST.get('country')
#      message=request.POST.get('subject')
#      contact.first_name=first_name
#      contact.last_name=last_name
#      contact.country=country
#      contact.message=message
#      contact.save()
#      return HttpResponse("<h1>Thanks for Contact Us</h1>")
#     return render(request,'contact.html')
def contact(request):
        if request.method=='POST':
         fname=request.POST['fname']
         lname=request.POST['lname']
         country=request.POST['country']
         subject=request.POST['subject']
         print(fname,lname,country,subject)
         contact=Contact(fname=fname,lname=lname,country=country,subject=subject)
         contact.save()
         #return HttpResponse("<h1>Thanks for Contact Us</h1>")
         messages.success(request, 'Form submit successfully')
        return render (request,'contact.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')