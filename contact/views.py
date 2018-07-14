from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

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
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			fn = request.POST.get('fn')
			ln = request.POST.get('ln')
			email = request.POST.get('email')
			content = request.POST.get('content')
			try:
				person = Person.objects.get(pk=email)
				person.first_name = fn
				person.last_name = ln
			except Person.DoesNotExist:
				person = Person(first_name=fn, last_name=ln, email=email)
			person.save()
			suggestion = PrivateSuggestion(suggestion=content, 
				pub_date=datetime.datetime.now(), person=person)
			suggestion.save()
			return HttpResponse('thank you')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form})