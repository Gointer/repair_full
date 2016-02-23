from django import forms
from .models import ContactModel


class ContactForm(forms):

	class Meta:
		models = ContactModel
		fields = ['name', 'email', 'subject', 'message']
