from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Character.models import Ability
from Charms.forms import CharmForm
from Charms.models import Charm


def basic_context():
    return {'charms': Charm.objects.all(),
            'abilities': Ability.objects.all()}  # Abilities could be reduced to a list of names


def save_new_instance(initialized_form, request):
    model_instance = initialized_form.save()  # write to database
    model_title = model_instance.__class__.__name__
    if request.is_ajax():
        msg = {'pk': model_instance.pk, 'title': str(model_instance), 'model': model_title, 'status': 'success'}
        return HttpResponse(json.dumps(msg), content_type="application/json")
    # return redirect('/%s/%i/' % (model_title, model_instance.pk))  # redirect to edit URL
    return redirect('/Charm/new/')


def initialize_from_existing_model(primary_key, request):
    """Raises an ObjectDoesNotExist exception when the primary_key is invalid"""
    model = Charm.objects.get(id=primary_key)  # may raise an exception
    initialized_form = CharmForm(request.POST or None, instance=model)
    return initialized_form, 'Charm'

def copy_charm(request, primary_key):
    model_name = 'Charm'
    try:
        initialized_form, model_name = initialize_from_existing_model(primary_key, request)
    except ObjectDoesNotExist:
        return redirect('/setup/%s/new/' % model_name)
    if initialized_form.is_valid() and request.method == 'POST':
        initialized_form.instance.pk = None  # This will cause a new instance to be created
        return save_new_instance(initialized_form, request)
    context = basic_context()
    context.update({'form': initialized_form,
                    'title': "Copy a " + model_name}.items())
    return render(request, 'Charms/new.html', context)


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



