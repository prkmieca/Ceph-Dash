

def get_erasure_details(cluster):

	#code_profiles = cluster.output.osdmap.erasure_code_profiles
	code_profiles = cluster['output']['osdmap']['erasure_code_profiles']
	return code_profiles