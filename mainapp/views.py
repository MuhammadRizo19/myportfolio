from django.shortcuts import render,redirect
from .models import Skill, Experience, AboutMe, Graduation, Service, Contact
from django.contrib import messages


def index(request):
    skills = Skill.objects.all()
    exper = Experience.objects.all()
    about = AboutMe.objects.all()
    graduation = Graduation.objects.all()
    service = Service.objects.all()

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        title = request.POST['title']
        message = request.POST['message']

        contact = Contact.objects.create(first_name=first_name,last_name=last_name,email=email,title=title,message=message)
        contact.save()
        messages.success(request, 'your message has been sent successfully ! ')
        return redirect('index')

    context = {
        'skills':skills,
        'exper':exper,
        'about':about,
        'graduation':graduation,
        'service':service,
    }
    return render(request, 'index.html', context)