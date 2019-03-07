from django.shortcuts import render,redirect
from .forms import ContactForm,Contact
# Create your views here.
def index(request):  #home page
    return render(request,'cwApp/index.html',)
def about(request): #About us page
    return render(request,'cwApp/aboutus.html',)
def gallery(request): #gallery
    return render(request,'cwApp/gallery.html',)
def resources(request):  #resources
    return render(request,'cwApp/resources.html',)

def contact(request):  #contact
    form=ContactForm(request.POST or None)
    if form.is_valid() and request.method =='POST':
        form.save()
        return redirect('submit')
    else:
        form=ContactForm(request.POST)
        context={
            'errors':form.errors,
            'form':form,
        }

    return render(request,'cwApp/contact.html',context)

def submit(request):
    return render(request,'cwApp/submit.html')

def secret(request):
    allModels=Contact.objects.all()
    return render(request,'cwApp/secret.html',{'allModels':allModels})



