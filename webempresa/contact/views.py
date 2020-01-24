from django.shortcuts import render, redirect
#Redirect sirve para poder redireccionar a otra pagina
from django.urls import reverse
#Es un metodo para q django acceda a una url dinamicamente
from django.core.mail import EmailMessage
# Es un metodo para configurar el envío de mails
from .forms import ContactForm

# Create your views here.
def contact(request):
    #Instanciamos el formulario antes de enviarlo al template:
    contact_form = ContactForm()
    #La plantilla se crea vacia. Ahora vemos si se envio algun dato en forma de POST
    if request.method == "POST":
        #Completamos el formulario con la data enviada:
        contact_form = ContactForm(data=request.POST)
        #Ahora queda el formulario rellenado.
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            #asignamos nombre con request post, y despues con get (leer) ponemos el nombre, o en su defecto si no hay nada vacio
            email = request.POST.get('email', '')
            contact = request.POST.get('content', '')
            #Agregamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió: \n\n{}".format(name, email, contact),
                "no-contestar@inbox.mailtrap.io",
                ["casal.juanmanuel@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
                #Algo no ha ido bien, redireccionamos a ok
            #redirigimos a contact agregando el parametro ok
    return render(request, "contact/contact.html", {'form':contact_form})