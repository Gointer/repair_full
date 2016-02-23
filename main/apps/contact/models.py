from django.db import models

# Create your models here.
class ContactModel(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100, db_index=True)
	subject = models.CharField(max_length=250, blank=True, null=True)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.email