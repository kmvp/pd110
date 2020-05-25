from django.shortcuts import render

# Create your views here.

def v_contacto(request):
	
	return render(request, "v_contacto.html", {})

def v_desayunos(request):
	
	return render(request, "v_desayunos.html", {})

def v_comidas(request):
	
	return render(request, "v_comidas.html", {})

def v_cenas(request):
	
	return render(request, "v_cenas.html", {})