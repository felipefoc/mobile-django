from django.shortcuts import render, redirect
from firstapp.integrations.jrapi import JrApi
from django.http import HttpResponse








def homePage(request):
    return render(request, 'templates/base.html', {}) 

def listPage(request):
    api = JrApi()
    allOrgs = api.get_orgs()
    page = 'listPage'
    context = {'allOrgs': allOrgs,
               'page': page }
    return render(request, 'templates/list.html', context)

def getPage(request):
    page = 'getPage'
    if request.method == 'POST':
        org = request.POST.get('input', False)
        if org:
            return redirect('get', org=org.lower())
    context = {'page': page }
    return render(request, 'templates/get.html', context)

def get(request, org, error=False):
    api = JrApi()
    data = api.create_and_get_org(org=org)
    if 'message' in data: # if error
        error = True
    page = 'getPage'
    context = {'page': page,
               'data': data,
               'error': error,
               'org': org,}
    return render(request, 'templates/org.html', context)

def delete(request, error=False):
    api = JrApi()
    org = request.POST.get('input'.lower(), False)
    if request.method == 'POST':        
        data = api.delete_org(org=org)
        if data.status_code == 404:
            error = True
        else:
            return redirect('listPage')
    page = 'delPage'
    context = {'page': page,
               'error': error,
               'name': org}
    return render(request, 'templates/delete.html', context)
