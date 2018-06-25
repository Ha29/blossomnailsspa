from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.views import generic

# Create your views here.
from .forms import ContactForm

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
			pass
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form})