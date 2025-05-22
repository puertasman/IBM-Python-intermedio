""" PAra el formulario """
from ast import AsyncFunctionDef
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    """ Página blog para noticias """
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '') 
            # Aquí enviaremos un correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {}<{}>\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["puertasman@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # todo ha ido bien.
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, mandamos a fail
                return redirect(reverse('contact')+"?fail")
            # Se supone que todo ha ido bien y redirigimos
            return redirect(reverse('contact')+"?ok")

    return render(request, 'contact/contact.html', {'form': contact_form}) 