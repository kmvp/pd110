from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
def _user_is_authenticated(user):
    # django < 2.0
    try:
        return user.is_authenticated()
    except TypeError:
        # django >= 2.0
        return user.is_authenticated

def inicio(request):
	titulo = "Formulario"
	#abc = "123"
	if _user_is_authenticated(request.user):
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	#print (dir(form)) es para ver en el cmd todo lo que se puede hacer con form
	
	context = {
		"titulo": titulo,
		#"abc": abc,
		"el_form": form,
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "Persona"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		if not nombre:
			context = {
				"titulo": "Gracias por registrarte %s!" %(email)
			}

		print (instance)
		print (instance.timestamp)
		# form_data = form.cleaned_data
		# abc = form_data.get("email")
		# abc2 = form_data.get("nombre")
		# obj = Registrado.objects.create(email=abc, nombre=abc2)

		#print (form_data.get("nombre"))
		#print (form_data.get("edad"))
		#print(form.cleaned_data)

	return render(request, "inicio.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.items():
		# 	print (key, value)
		# for key in form.cleaned_data:
		# 	print (key)
		# 	print (form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "otroemail@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)
		# print (email, mensaje, nombre)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)