from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import ProjectForm, ServiceForm, BlogPostForm, ContactForm, LoginForm
from .models import *

# Create your views here.


def home(request):
    data = Service.objects.all()
    proj = Project.objects.all()
    blog = BlogPost.objects.all()
    return render(request,'index.html', {'data':data, 'proj':proj, 'blog':blog})


def about(request):
    return render(request, 'about.html')

def services(request):
    data = Service.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to success URL
    else:
        form = ServiceForm()
    return render(request, 'services.html',{'data':data, 'form':form})

def projects(request):
    proj = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to success URL
    else:
        form = ProjectForm()
    return render(request, 'projects.html',{'proj':proj, 'form':form})

def blog(request):
    blog = BlogPost.objects.all()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to success URL
    else:
        form = BlogPostForm()
    return render(request, 'blog.html', {'blog':blog, 'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            try:
                # Send email to website owner
                email_subject = 'New Contact Form Submission'
                email_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
                email = EmailMessage(email_subject, email_body, to=[settings.CONTACT_EMAIL])
                email.send()

                # Send confirmation email to the person
                confirmation_subject = 'Thanks for contacting us'
                confirmation_body = 'We have received your message. Our team will get back to you soon.'
                confirmation_email = EmailMessage(confirmation_subject, confirmation_body, to=[email])
                confirmation_email.send()

                return render(request, 'contact_success.html')  # Render a success page
            except Exception as e:
                print(e)  # Handle email sending errors
                return render(request, 'contact_error.html')  # Render an error page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
    
    