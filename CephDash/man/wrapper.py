import requests

def list(endpoint, headers):	
	url = endpoint+'/report'
	r = requests.get(url, headers=headers)

	data = r.json()
	return data

def list_osds(endpoint, headers):
	url = endpoint+'/node/ls?type=osd'
	r = requests.get(url, headers=headers)

	data = r.json()

	return data

def add_replicated_pool(endpoint, entry_name, entry_size, entry_pg, entry_type, entry_rule_set):

	if entry_size == '2':
		payload = {'pool': entry_name, 'pg_num': entry_pg, 'pgp_num': entry_pg, 'pool_type': entry_type, 'ruleset': entry_rule_set}
		r = requests.put(endpoint+'/osd/pool/create', params=payload)

	else:
		payload = {'pool': entry_name, 'pg_num': entry_pg,'pool_type': entry_type, 'ruleset': entry_rule_set}
		r = requests.put(endpoint+'/osd/pool/create', params=payload)

		payload = {'pool': entry_name, 'var': 'size', 'val': entry_size}
		r = requests.put(endpoint+'/osd/pool/set', params=payload)


def add_erasured_pool(endpoint, entry_name, entry_pg, entry_type, entry_rule_set, entry_code_profile):

		payload = {'pool': entry_name, 'pg_num': entry_pg, 'pgp_num': entry_pg, 'pool_type': entry_type, 'erasure_code_profile': entry_code_profile, 'ruleset': entry_rule_set}
		r = requests.put(endpoint+'/osd/pool/create', params=payload)


def del_pool(endpoint, data):
	payload = {'pool': data, 'pool2': data, 'sure': '--yes-i-really-really-mean-it'}
	r = requests.delete(endpoint+'/osd/pool/delete', params=payload)

def edit_replicated_pool(endpoint, src_pool, entry_name, entry_size, entry_pgs, entry_rule_set_simple):

	#rename
	if src_pool != entry_name:
		print('COMPARING NAMES')
		payload = {'srcpool': src_pool, 'destpool': entry_name}
		r = requests.put(endpoint+'/osd/pool/rename', params=payload)
		src_pool = entry_name

	print('NO RENAME')
	#size
	payload = {'pool': src_pool, 'var': 'size', 'val': entry_size}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)
	#pg_num
	payload = {'pool': src_pool, 'var': 'pg_num', 'val': entry_pgs}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)

	payload = {'pool': src_pool, 'var': 'pgp_num', 'val': entry_pgs}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)


	#ruleset
	payload = {'pool': src_pool, 'var': 'crush_ruleset', 'val': entry_rule_set_simple}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)

def edit_erasured_pool(endpoint, src_pool, entry_name, entry_pgs, entry_rule_set_erasured):

	#rename
	if src_pool != entry_name:
		print('COMPARING NAMES')
		payload = {'srcpool': src_pool, 'destpool': entry_name}
		r = requests.put(endpoint+'/osd/pool/rename', params=payload)
		src_pool = entry_name

	print('NO RENAME')

	#pg_num
	payload = {'pool': src_pool, 'var': 'pg_num', 'val': entry_pgs}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)

	payload = {'pool': src_pool, 'var': 'pgp_num', 'val': entry_pgs}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)

	#ruleset
	payload = {'pool': src_pool, 'var': 'crush_ruleset', 'val': entry_rule_set_erasured}
	r = requests.put(endpoint+'/osd/pool/set', params=payload)


def set_pool_quotas(endpoint, pool_name, entry_max_objects, entry_max_bytes):

	#max_objects
	payload = {'pool': pool_name, 'field': 'max_objects', 'val': entry_max_objects}
	r = requests.put(endpoint+'/osd/pool/set-quota', params=payload)

	#max_bytes
	payload = {'pool': pool_name, 'field': 'max_bytes', 'val': entry_max_bytes}
	r = requests.put(endpoint+'/osd/pool/set-quota', params=payload)

def make_snapshot(endpoint, entry_snap, pool_name):

	payload = {'pool': pool_name, 'snap': entry_snap}
	r = requests.put(endpoint+'/osd/pool/mksnap', params=payload)

def remove_snapshot(endpoint, entry_snap_list, pool_name):

	for snapshot in entry_snap_list:
		payload = {'pool': pool_name, 'snap': snapshot}
		r = requests.put(endpoint+'/osd/pool/rmsnap', params=payload)

def osd_reweight(endpoint, osd, weight):

	payload = {'id': osd, 'weight': weight}
	r = requests.put(endpoint+'/osd/reweight', params=payload)

def osd_repair(endpoint, osd):

	payload = {'who': osd}
	r = requests.put(endpoint+'/osd/repair', params=payload)

def osd_in(endpoint, osd):

	payload = {'ids': osd}
	r = requests.put(endpoint+'/osd/in', params=payload)

def osd_out(endpoint, osd):

	payload = {'ids': osd}
	r = requests.put(endpoint+'/osd/out', params=payload)

def osd_down(endpoint, osd):

	payload = {'ids': osd}
	r = requests.put(endpoint+'/osd/down', params=payload)

def osd_settings(endpoint, unsetList, setList):

	for key in unsetList:
		payload = {'key': key}
		r = requests.put(endpoint+'/osd/unset', params=payload)

	for key in setList:
		payload2 = {'key': key}
		r = requests.put(endpoint+'/osd/set', params=payload2)

def create_erasure_code_profile(endpoint, erasure_name, object_chunks, coding_chunks):

	prep = '[k['+object_chunks+']m['+coding_chunks+']]'
	payload = {'name': erasure_name, 'profile': prep}
	r = requests.put(endpoint+'/osd/erasure-code-profile/set', params=payload)

def delete_erasure_code_profile(endpoint, erasure_name):

	payload = {'name': erasure_name}
	r = requests.put(endpoint+'/osd/erasure-code-profile/rm', params=payload)


def crush_tree_list(endpoint, headers):
	url = endpoint+'/osd/crush/tree'
	r = requests.get(url, headers=headers)

	data = r.json()
	return data

def create_bucket(endpoint, headers, bucket, bucket_type, bucket_root, bucket_rack):

	payload = {'name': bucket, 'type': bucket_type}
	url = endpoint+'/osd/crush/add-bucket'
	url2 = endpoint+'/osd/crush/move'

	if bucket_type == 'root':

		r = requests.put(url, params=payload)

	elif bucket_type == 'rack':

		r = requests.put(url, params=payload)
		payload = {'name': bucket, 'args': 'root='+bucket_root}
		r = requests.put(url2, params=payload)

	else:
		r = requests.put(url, params=payload)
		payload = {'name': bucket, 'args': 'rack='+bucket_rack}
		r = requests.put(url2, params=payload)

def move_host(endpoint, host_name, chassis):

	if chassis == 'default':
		payload = {'name': host_name, 'args': 'root='+chassis}
		r = requests.put(endpoint+'/osd/crush/move', params=payload)
	else:
		payload = {'name': host_name, 'args': 'chassis='+chassis}
		r = requests.put(endpoint+'/osd/crush/move', params=payload)

def add_crush_rule(endpoint, rule_name, rule_type, root_name, ptype, code):

	if rule_type == 'replicated':

		payload = {'name': rule_name, 'root': root_name, 'type': ptype}
		r = requests.put(endpoint+'/osd/crush/rule/create-simple', params=payload)

	else:

		payload = {'name': rule_name, 'profile': code}
		r = requests.put(endpoint+'/osd/crush/rule/create-erasure', params=payload)

def delete_bucket(endpoint, bucket):

	payload = {'name': bucket}
	r= requests.put(endpoint+'/osd/crush/rm', params=payload)

def del_crush_rule(endpoint, rule_name):

	payload = {'name': rule_name}
	r = requests.put(endpoint+'/osd/crush/rule/rm', params=payload)


