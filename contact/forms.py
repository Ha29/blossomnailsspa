from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Person

class ContactForm(forms.Form):
	fn = forms.CharField(required=True, max_length=20, 
		widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	ln = forms.CharField(required=True, max_length=20, 
		widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email = forms.EmailField(required=True, max_length=254, 
		widget=forms.EmailInput(
			attrs={'placeholder': 'someone@example.com'}))
	# person = Person(first_name = contact_first_name,
	# 	last_name=contact_last_name, email=contact_email)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea(
			attrs={'placeholder': 'Write your suggestion here'}))

	def clean_recipient(self, email):
		try:
			validate_email(email)
			print("cleaned right")
			return True
		except ValidationError:
			print("cleaned incorrectly")
			return False

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		fn = cleaned_data.get('fn')
		ln = cleaned_data.get('ln')
		email = cleaned_data.get('email')
		if not self.clean_recipient(email):
			raise forms.ValidationError("Incorrect Email")
		elif not ln or not fn:
			raise forms.ValidationError("Enter alphabetical only")
		print("worked")