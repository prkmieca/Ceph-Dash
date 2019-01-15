from django import forms
from . import wrapper

pools = wrapper.list_pools()

def populate_editForm(endpoint, headers, poolName):
	pools = list_pools(endpoint, headers)
	formContent = {}
	for pool in pools:
		if pool.pool_name == poolName:
		formContent = pool
		return formContent
		else
		return 
		return formContent


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
