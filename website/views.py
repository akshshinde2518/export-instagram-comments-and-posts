from django.http import HttpResponse
from django.shortcuts import redirect, render

from website import models

# Create your views here.

def home(req):
    hero =models.Hero.objects.all()
    about =models.About.objects.all()
    skills =models.Skills.objects.all()
    resume =models.Resume.objects.all()
    portfolio =models.Portfolio.objects.all()
    testimonials =models.Testimonials.objects.all()
    contacts =models.Contact.objects.all()
    obj = {"hero":hero,"about":about,"skills":skills,"resume":resume,"portfolio":portfolio,"testimonials":testimonials,"contacts":contacts}
    return render(req,"home.html",obj)

def save_message(req):
    message = models.Message(
        user_name = req.POST['user_name'],
        user_email = req.POST['user_email'],
        user_subject = req.POST['user_subject'],
        user_message = req.POST['user_message']
    )
    message.save()
    return redirect('/')
   

