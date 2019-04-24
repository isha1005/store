from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import About, FAQ

def home(request):
    return render(request,'startup/home.html', {'title': 'Home'})


def about(request):
    context ={
        'about': About.objects.get(title='About Us')
    }
    return render(request, 'startup/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('startup-home')
    else:
        form = ContactForm()
    return render(request,'startup/contact.html', {'form': form})


def faq(request):
    context = {
        'faqs': FAQ.objects.all()
    }
    return render(request, 'startup/faq.html', context)


def amenities(request):
    return render(request,'startup/amenities.html', {'title': 'Amenities'})

def plan(request):
    return render(request, 'startup/plan.html', {'title': 'Plans'})
