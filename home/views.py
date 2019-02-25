from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import PrivateSuggestion, Person
from .forms import ContactForm

import datetime, uuid

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
	list_data = get_data_in_list('static/home.json')
	if request.method == 'POST':
		print("post-request")
		form = ContactForm(request.POST)
		if form.is_valid():
			print("valid!")
			fn = request.POST.get('first_name')
			ln = request.POST.get('last_name')
			email = request.POST.get('email')
			content = request.POST.get('content')
			try:
				person = Person.objects.get(pk=email)
				person.first_name = fn
				person.last_name = ln
			except (Person.DoesNotExist, ProgrammingError) as error:
				person = Person(first_name=fn, last_name=ln, email=email)
			person.save()
			suggestion = PrivateSuggestion(suggestion=content, 
				pub_date=datetime.datetime.now(), person=person)
			suggestion.save()
			new_form = ContactForm()
			return render(request, 'index.html', \
				{'src_names': names, 'contents': list_data, \
				'form': new_form, 'accepted':1})
	else:
		form = ContactForm()
	return render(request, 'index.html', \
			{'src_names': names, 'contents': list_data, \
			'form': form, 'accepted': 0})
	# return render(request, 'index.html', \
	# 		{'src_names': names, 'contents': list_data, \
	# 		'accepted': 0})

def services(request):
	list_data = get_data_in_list('static/services.json')
	return render(request, 'services.html', \
		{'contents': list_data})


	
def handler404(request):
	return render(request, 'index.html')

def handler505(request):
	return render(request, 'index.html')

def handler500(request):
	return HttpResponseRedirect("/")

def get_data_in_list(path):
	data = open(path).read()
	jsonData = json.loads(data)
	list_data = [line.strip('\n') for line in jsonData['contents']]
	return enumerate(list_data)



