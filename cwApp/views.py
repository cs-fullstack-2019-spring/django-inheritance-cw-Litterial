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
    form=ContactForm(request.POST or None) #get
    context={
        'form':form,
    }
    if request.method =='POST':  #if post request
        if form.is_valid():   #if valid form
            form.save()
            return redirect('submit')
        else:  #otherwise an error message will appear after they submit the form
            form=ContactForm(request.POST)
            context={
                'errors':form.errors,
                'form':form,
            }
            return render(request,'cwApp/contact.html',context)
    return render(request,'cwApp/contact.html',context)


def submit(request): #conformation page
    return render(request,'cwApp/submit.html')

def secret(request):
    allModels=Contact.objects.all()
    return render(request,'cwApp/secret.html',{'allModels':allModels})



