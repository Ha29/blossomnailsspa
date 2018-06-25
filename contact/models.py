from django.db import models

# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)
	is_admin = models.BooleanField()

"""
All the object foreign keys use on_delete=models.PROTECT because
we want to make sure these are not deleted when the objects that use it 
are deleted. For example, deleting an answer should not delete the
question that the answer was placed on it. Deleting a Question should
not delete the person that asked the question. 
"""
class Choice(models.Model):
	text = ["Private", "Public"]

class PrivateSuggestion(models.Model):
	suggestion = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	person = models.ForeignKey(Person, on_delete=models.PROTECT)

class PrivateResponse(models.Model):
	suggestion = models.ForeignKey(PrivateSuggestion, on_delete=models.PROTECT)
	answer_text = models.CharField(max_length=200)
	person = models.ForeignKey(Person, on_delete=models.PROTECT)
	res_date = models.DateTimeField('response date')

class PublicQuestion(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	person = models.ForeignKey(Person, on_delete=models.PROTECT)

class PublicAnswer(models.Model):
	public_question = models.ForeignKey(PublicQuestion, models.PROTECT)
	answer_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	person = models.ForeignKey(Person, on_delete=models.PROTECT)

