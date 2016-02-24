from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):

	class Meta:
		model = ContactModel
		fields = ['name', 'email', 'subject', 'message']

		widgets ={
			'name':	forms.TextInput(
                attrs={'type': "text",'name':"name",  'placeholder':"Ваше Имя*", 'class':"form-control input-box", 'id':"name"}
            ),

			'email': forms.EmailInput(
                attrs={'name':"email",  'placeholder':"Ваше Email*", 'class':"form-control input-box", 'id':"email"},
            ),

			'subject': forms.TextInput(
                attrs={'name':"subject",  'placeholder':"Тема", 'class':"form-control input-box", 'id':"subject"}
            ),

			'message':	forms.Textarea(
                attrs={'name':"message",  'placeholder':"Ваше Сообщение*", 'class':"form-control input-box", 'id':"message"}
            ),
		}