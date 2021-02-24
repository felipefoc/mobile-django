from django.shortcuts import render, redirect
from firstapp.integrations.jrapi import JrApi




api = JrApi()

def homePage(request):
    return render(request, 'templates/base.html', {}) 

def listPage(request):
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
            return redirect('get', org=org)
    context = {'page': page }
    return render(request, 'templates/get.html', context)

def get(request, org):
    data = api.create_and_get_org(org=org)
    page = 'getPage'
    context = {'page': page,
               'data': data}
    return render(request, 'templates/org.html', context)

def delete(request, error=False):
    org = request.POST.get('input', False)
    if request.method == 'POST':        
        data = api.delete_org(org=org)
        if data.status_code == 404:
            error = True
        else:
            return redirect('listPage')
    page = 'delPage'
    context = {'page': page,
               'error': error}
    return render(request, 'templates/delete.html', context)
