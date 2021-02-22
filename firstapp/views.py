from django.shortcuts import render
from firstapp.integrations.jrapi import JrApi


api = JrApi()

def first_view(request):
    allOrgs = api.get_orgs()
    context = {'allOrgs' : allOrgs}
    return render(request, 'templates/firstapp.html', context)