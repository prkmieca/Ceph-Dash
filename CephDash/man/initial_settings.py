
def initial():


	flag = {
    'name': 'cluster',
    'class1': 'active',
    'class2': 'show'
}


	osd_flag = {
    'hostname': 'none'
}

	headers = {'Accept': 'application/json'}
	endpoint = 'http://0.0.0.0:5000/api/v0.1'

	return flag, osd_flag, headers, endpoint