import requests

def cluster_status():

	url = 'http://0.0.0.0:5000/api/v0.1/status'
	headers = {'Accept': 'application/json'}
	r = requests.get(url, headers=headers)

	data = r.json()
	return data
