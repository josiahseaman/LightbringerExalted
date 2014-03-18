from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Charms.forms import CharmForm


def save_new_instance(initialized_form, request):
    model_instance = initialized_form.save()  # write to database
    model_title = model_instance.__class__.__name__
    if request.is_ajax():
        msg = {'pk': model_instance.pk, 'title': str(model_instance), 'model': model_title, 'status': 'success'}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    return redirect('/setup/%s/%i/' % (model_title, model_instance.pk))  # redirect to edit URL


def new_form(request, initialized_form, context):
    if initialized_form.is_valid():
        return save_new_instance(initialized_form, request)
    return render(request, 'Charms/new.html', context)  # render in validation error messages


def new_charm(request):
    initialized_form = CharmForm(request.POST or None)
    context = {'title': 'Describe a Charm with Traits'}
    return new_form(request, initialized_form, context)
