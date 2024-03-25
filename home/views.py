from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import About, Gallery, Versions, Home, Contact


def home(request):
    if request.method == 'POST':
        # print(request.POST.get('ism'))
        name = request.POST.get('ism')
        number = request.POST.get('number')
        message = request.POST.get('message')
        if name or not number or not message:
            Contact.objects.create(name=name, phone=number, message=message)
            messages.success(request, 'Muvaffaqiyatli saqlandi!')
            return redirect(reverse('home'))

        else:
            return redirect(reverse('home'))

    homes = Home.objects.all()
    about = About.objects.all()
    gallerys = Gallery.objects.all()
    versias = Versions.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'base.html', {'homes': homes, 'about': about, 'gallerys': gallerys, 'versias': versias,
                                         'contacts': contacts}, )


def contact(request):
    if request.method == 'POST':
        print(request.POST('ism'))
        return redirect(reverse('success'))  # Redirect to the 'success' view

    return render(request, 'contact.html', )


def success(request):
    return render(request, 'success.html')


def success(request):
    return render(request, 'success.html')
