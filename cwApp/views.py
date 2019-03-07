from django.shortcuts import render

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
    return render(request,'cwApp/contact.html',)





