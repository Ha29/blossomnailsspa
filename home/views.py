from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

app_name = "home"
# Create your views here.
def index(request):
	# return HttpResponse("You're at the Blossom Nails Spa home page")
	return render(request, 'index.html')

def handler404(request):
	return render(request, 'index.html')

def handler505(request):
	return render(request, 'index.html')

def handler500(request):
	return HttpResponseRedirect("/")



