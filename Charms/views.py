from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Charms.forms import CharmForm
from Charms.models import Charm


def list_charms_by_ability():
    Charm.objects.all()
# from django.db.models import Count
# pubs = Publisher.objects.annotate(num_books=Count('book'))


def basic_context():
    return {'charms': list_charms_by_ability()}

def save_new_instance(initialized_form, request):
    model_instance = initialized_form.save()  # write to database
    model_title = model_instance.__class__.__name__
    if request.is_ajax():
        msg = {'pk': model_instance.pk, 'title': str(model_instance), 'model': model_title, 'status': 'success'}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    # return redirect('/%s/%i/' % (model_title, model_instance.pk))  # redirect to edit URL
    return redirect('/Charm/new/')


def new_form(request, initialized_form, context):
    if initialized_form.is_valid():
        return save_new_instance(initialized_form, request)
    return render(request, 'Charms/new.html', context)  # render in validation error messages


def new_charm(request):
    initialized_form = CharmForm(request.POST or None)
    context = basic_context()
    context['form'] = initialized_form
    context['title'] = 'Describe a Charm with Traits'
    return new_form(request, initialized_form, context)


def edit_charm(request, primary_key):
    try:
        existing_charm = Charm.objects.get(pk=primary_key)
    except ObjectDoesNotExist:
        return redirect('/Charm/new/')
    initialized_form = CharmForm(request.POST or None, instance=existing_charm)
    if initialized_form.is_valid() and request.method == 'POST':
        initialized_form.save()  # write instance updates to database
    context = basic_context()
    context['form'] = initialized_form
    context['title'] = "Edit an Existing Charm"
    context['summary'] = str(existing_charm)
    return render(request, 'Charms/new.html', context)



