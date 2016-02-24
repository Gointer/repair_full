import json

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm


class HomePageView(TemplateView):
	template_name = "base.html"



def create_contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)

		if contact_form.is_valid():
			model_instance = contact_form.save()
		#	model_instance


	return HttpResponse()

