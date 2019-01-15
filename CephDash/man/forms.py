from django import forms
from . import wrapper

class addPoolForm(forms.Form):
	pool = forms.CharField(label='Pool name', max_length=100, widget=forms.TextInput(
		attrs=
		{'class': 'form-control',
		'placeholder': 'Enter pool name'}))

	pg_num = forms.CharField(label='Pool size', max_length=100, widget=forms.TextInput(
		attrs=
		{'class': 'form-control',
		'placeholder': 'Enter pool size',
		}
		))
