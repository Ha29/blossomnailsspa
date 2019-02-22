from django.db import models

# Create your models here.


class Person(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(primary_key=True, max_length=254)
	is_admin = models.BooleanField(default=False)

class PrivateSuggestion(models.Model):
	suggestion = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	person = models.ForeignKey(Person, on_delete=models.PROTECT)