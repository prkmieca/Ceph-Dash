from django.shortcuts import render
from django.http import HttpResponse
from . import wrapper
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):

    return render(request, 'templates/login.html')

def log_in(request):
    if request.method == "POST":

        username =  request.POST.get('name', 'no_name')
        password = request.POST.get('pass', 'no_pass')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print("OK LOGIN")
            login(request, user)

            return HttpResponseRedirect('/dash/')
        
        else:
            # Return an 'invalid login' error message.
            print("NO LOGIN")
            return HttpResponseRedirect('/login/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')
        
@login_required
def index2(request):
    cluster_status = wrapper.cluster_status()
    #print(cluster_status)

    context = { 'cluster_status': cluster_status}
    return render(request, 'templates/base.html', context)
