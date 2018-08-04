from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.utils import ProgrammingError

from django.views.generic.edit import FormView
from django.views import generic

# Create your views here.
from .forms import ContactForm
from .models import PrivateSuggestion, Person

import datetime, uuid

app_name = "contact"
# def ContactView(FormView):
# 	template_name = 'contact.html'
# 	form_class = ContactForm
# 	success_url = '/thanks/'

# 	def get(self, *args, **kwargs):
# 		return HttpResponse("Bitch") 

# 	def form_valid(self, form):
# 		# form.send_email()
# 		return HttpResponse('valid')

# 	def form_invalid(self, form):
# 		return HttpResponse('invalid')

def function(request):
	# form = ContactForm()
	# if request.method == 'POST':
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('function')
	# 	else:
	# 		return HttpResponse('Error!')
	# context = {'form': form}
	# return render(request, 'contact.html', context)
	print("contact-form")
	if request.method == 'POST':
		print("post-request")
		form = ContactForm(request.POST)
		if form.is_valid():
			print("valid!")
			fn = request.POST.get('fn')
			ln = request.POST.get('ln')
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
			return render(request, 'contact.html', {'form': new_form, 'accepted': 1})
		print("invalid")
	else:
		print("still in contact form")
		form = ContactForm()
	print("render with old information")
	return render(request, 'contact.html', {'form': form, 'accepted': 0})