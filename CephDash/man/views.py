from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from . import wrapper, flags, e_codes
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

#######################################################
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
# Create your views here.
@login_required
def index(request):


    cluster = wrapper.list(endpoint, headers)
    osds_list = wrapper.list_osds(endpoint, headers)
    code_profiles = e_codes.get_erasure_details(cluster)

    OSDflags = flags.get_flags(cluster)
    crushTree = wrapper.crush_tree_list(endpoint, headers)

    print(osds_list)
    #nodes = wrapper.list_nodes(endpoint, headers)

    #print (cluster)
    print(flag['name'])
    context = { #'nodes': nodes,
                'cluster': cluster,
                'osds_list': osds_list,
                'flag': flag,
                'osd_flag': osd_flag,
                'OSDflags': OSDflags,
                'crushTree': crushTree,
                'code_profiles': code_profiles}

    return render(request, 'templates/manage2.html', context)

@login_required
def addPool (request):
    if request.method == "POST":
        entry_name = request.POST.get("name", "default")
        entry_size = request.POST.get("size", "2")
        entry_pg = request.POST.get("pg_num", "64")
        entry_type = request.POST.get("inlineRadioOptions", "replicated")
        entry_rule_set_simple = request.POST.get("rulesRep", "0")
        entry_rule_set_erasured = request.POST.get("rulesEra", "0")
        entry_code_profile = request.POST.get("code_profiles", "default")


        if entry_type == 'replicated':
            print("Create replicated pool.")
            print(entry_name)
            print(entry_size)
            print(entry_pg)
            print(entry_type)
            print(entry_rule_set_simple)
            wrapper.add_replicated_pool(endpoint, entry_name, entry_size, entry_pg, entry_type, entry_rule_set_simple)

        elif entry_type == 'erasure':
            print("Create erasured pool.")
            print(entry_name)
            print(entry_pg)
            print(entry_type)
            print(entry_rule_set_erasured)
            print(entry_code_profile)
            wrapper.add_erasured_pool(endpoint, entry_name , entry_pg, entry_type, entry_rule_set_erasured, entry_code_profile)

        else:
            print("No pool type.")



        flag['name'] = 'pools'
        return HttpResponseRedirect('/manage/')


    return HttpResponseRedirect('/manage/')

@login_required
def delPool(request, poolName):
    if request.method == "POST":
        wrapper.del_pool(endpoint, poolName)

        flag['name'] = 'pools'
        return HttpResponseRedirect('/manage/')
    

    return HttpResponseRedirect('/manage/')

@login_required
def editPool(request, poolName, poolType):
    if request.method == "POST":
        src_pool = poolName

        entry_name= request.POST.get("var1", "default")
        entry_size = request.POST.get("var2", "default")
        entry_pgs = request.POST.get("var3", "default")
        entry_rule_set_simple = request.POST.get("rulesRep", "0")
        entry_rule_set_erasured = request.POST.get("rulesEra", "0")


        if poolType == '1':
            print("Edit replicated pool.")
            print(entry_name)
            print(entry_size)
            print(entry_pgs)
            print(entry_rule_set_simple)
            wrapper.edit_replicated_pool(endpoint, src_pool, entry_name, entry_size, entry_pgs, entry_rule_set_simple)

        elif poolType == '3':
            print("Edit erasured pool.")
            print(entry_name)
            print(entry_pgs)
            print(entry_rule_set_erasured)
            wrapper.edit_erasured_pool(endpoint, src_pool, entry_name, entry_pgs, entry_rule_set_erasured)

        else:
            print("No pool type.")

        #wrapper.edit_pool(endpoint, src_pool, entry_name,  entry_size, entry_pgs)
        flag['name'] = 'pools'


    return HttpResponseRedirect('/manage/')

@login_required
def setQuota(request, poolName):
    if request.method == "POST":
        pool_name = poolName

        entry_max_objects = request.POST.get("var1", "0")
        entry_max_bytes  = request.POST.get("var2", "0")

        wrapper.set_pool_quotas(endpoint, pool_name, entry_max_objects,  entry_max_bytes)
        flag['name'] = 'pools'


    return HttpResponseRedirect('/manage/')

@login_required
def makeSnap(request, poolName):
    if request.method == "POST":
        pool_name = poolName
        entry_snap = request.POST.get("var1", "snapshot")
        wrapper.make_snapshot(endpoint, entry_snap, pool_name)
        flag['name'] = 'pools'


    return HttpResponseRedirect('/manage/')

@login_required
def removeSnap(request, poolName):
    if request.method == "POST":
        pool_name = poolName
        entry_snap_list = request.POST.getlist("checkDelSnap")

        wrapper.remove_snapshot(endpoint, entry_snap_list, pool_name)
        flag['name'] = 'pools'


    return HttpResponseRedirect('/manage/')

@login_required
def osdSettings(request):
    if request.method == "POST":
        setList = request.POST.getlist("check")
        unsetList = ['pause', 'noup', 'nodown', 'noout', 'noin', 'nobackfill', 'norecover', 'noscrub', 'nodeep-scrub']
        #unsetList = all_settings

        for x in setList:
            if x in unsetList:
                unsetList.remove(x)

        wrapper.osd_settings(endpoint, unsetList, setList)
        #entry_pause = request.POST.get("checkPause", "default")
        #entry_noup = request.POST.get("checkNoup", "default")
        #entry_checkNodown = request.POST.get("checkNodown", "default")
        #print(entry_pause+' '+entry_noup+' '+entry_checkNodown)
        #wrapper.cluster_osd_set(endpoint, setList, unsetList)
        flag['name'] = 'cluster'


    return HttpResponseRedirect('/manage/')

@login_required
def reweight(request, osdID, hostname):
    if request.method == 'POST':
        weight = request.POST.get("weight", "1.0")
        osd = osdID
        host = hostname
        print(hostname)

        wrapper.osd_reweight(endpoint, osd, weight)
        flag['name'] = 'osds'
        osd_flag['hostname'] = host

    return HttpResponseRedirect('/manage/')

@login_required
def osdRepair(request, osdID, hostname):
    osd = osdID
    host = hostname
    wrapper.osd_repair(endpoint, osd)
    flag['name'] = 'osds'
    osd_flag['hostname'] = host

    return HttpResponseRedirect('/manage/')

@login_required
def osdIn(request, osdID, hostname):
    osd = osdID
    host = hostname
    wrapper.osd_in(endpoint, osd)
    flag['name'] = 'osds'
    osd_flag['hostname'] = host

    return HttpResponseRedirect('/manage/')

@login_required
def osdOut(request, osdID, hostname):
    osd = osdID
    host = hostname
    wrapper.osd_out(endpoint, osd)
    flag['name'] = 'osds'
    osd_flag['hostname'] = host

    return HttpResponseRedirect('/manage/')

@login_required
def osdDown(request, osdID, hostname):
    osd = osdID
    host = hostname
    wrapper.osd_down(endpoint, osd)
    flag['name'] = 'osds'
    osd_flag['hostname'] = host

    return HttpResponseRedirect('/manage/')

@login_required
def addErasure(request):
    if request.method == 'POST':
        erasure_name = request.POST.get("name", "erasure")
        object_chunks = request.POST.get("k", "2")
        coding_chunks = request.POST.get("m", "1")


        wrapper.create_erasure_code_profile(endpoint, erasure_name, object_chunks, coding_chunks)

        flag['name'] = 'erasure'

    return HttpResponseRedirect('/manage/')

@login_required
def delErasure(request, erasure):
    if request.method == 'POST':
        erasure_name = erasure

        wrapper.delete_erasure_code_profile(endpoint, erasure_name)
        flag['name'] = 'erasure'

    return HttpResponseRedirect('/manage/')

@login_required
def addBucket(request):
    if request.method == 'POST':
        entry_name = request.POST.get("name", "no_name")
        entry_type = request.POST.get("inlineRadioOptions", "no_type")
        entry_root = request.POST.get("root", "no_root")
        entry_rack = request.POST.get("rack", "no_rack")

        wrapper.create_bucket(endpoint, headers, entry_name, entry_type, entry_root, entry_rack)


    flag['name'] = 'crush'

    return HttpResponseRedirect('/manage/')
    
@login_required
def addCrushRule(request):
    if request.method == 'POST':

        entry_rule_type = request.POST.get("inlineRadioOptions", "no_rule_type")
        entry_name = request.POST.get("name", "no_name")
        entry_root = request.POST.get("root", "no_root")
        entry_ptype = request.POST.get("p_tye", "no_type")
        entry_code = request.POST.get("code_profile", "no_code")

        wrapper.add_crush_rule(endpoint, entry_name, entry_rule_type, entry_root, entry_ptype, entry_code)


    flag['name'] = 'crush'

    return HttpResponseRedirect('/manage/')

@login_required    
def moveHost(request):
    if request.method == 'POST':
        entry_host = request.POST.get("host", "no_host")
        entry_chassis = request.POST.get("chassis", "no_chassis")

        wrapper.move_host(endpoint, entry_host, entry_chassis)

    flag['name'] = 'crush'

    return HttpResponseRedirect('/manage/')

@login_required
def delBucket(request):
    if request.method == 'POST':
        entry_name = request.POST.get("bucket", "no_name")

        wrapper.delete_bucket(endpoint, entry_name)

    flag['name'] = 'crush'

    return HttpResponseRedirect('/manage/')

@login_required
def delRule(request):
    if request.method == 'POST':
        entry_name = request.POST.get("rule", "no_name")

        wrapper.del_crush_rule(endpoint, entry_name)

    flag['name'] = 'crush'

    return HttpResponseRedirect('/manage/')