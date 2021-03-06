# Create your views here.
#　coding: utf8
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render

# app specific files

from models import *
from forms import *
import datetime
from django.db import transaction
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def info_input_view(request):
    print request.POST.get('username', False)
    user = authenticate(username=request.POST.get('username', False), password=request.POST.get('password', False))
    print request.user
    form = PersonalForm(request.POST or None)

    t = get_template('info/info_input.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def save_personal_info(request):
    #print "press create"
    form = PersonalForm(request.POST or None)
    if form.is_valid():
        p = form.save(commit=False)
        p.save()
        #for orders_id in form.cleaned_data.get('orders'):
        form = ProductForm()

    t = get_template('info/info_input.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

