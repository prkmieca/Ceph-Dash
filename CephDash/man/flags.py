
def get_flags(cluster):
	
	all_flags = cluster['output']['osdmap']['flags']
	all_flags.split(',')
	return all_flags