# from django import forms
# from .models import Participant

# class Result(forms.ModelForm):
# 	class Meta:
# 		model = Participant
# 		fields = '__all__'

from django.forms import ModelForm
from .models import Payment


class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields = '__all__'