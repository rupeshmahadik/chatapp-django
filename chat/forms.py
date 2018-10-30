from django import forms
from .models import chatter

class chatterForm(forms.ModelForm):
	
	class Meta:
		model = chatter
		fields = [

			
			"chat_field",
			]
