from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

app_name = "home"
# Create your views here.
def index(request):
	# return HttpResponse("You're at the Blossom Nails Spa home page")
	# string_left = "<div class=\"caro-image\"></div>{\% load staticfiles" + \
	# 	" \%}<img src=\"{\% static '"
	# string_right = ".jpg' \%}\"></div>"
	names = []
	for i in range(1, 18):
		string = 'home/images/' + str(i) + '.jpg'
		names.append(string)
	return render(request, 'index.html', {'src_names': names})

def services(request):
	return render(request, 'services.html')

def gallery(request):
	return render(request, 'gallery.html')
	
def handler404(request):
	return render(request, 'index.html')

def handler505(request):
	return render(request, 'index.html')

def handler500(request):
	return HttpResponseRedirect("/")



