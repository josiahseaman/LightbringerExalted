from django.shortcuts import render

"""For Dynamically adding new items to a list of forms:
http://stackoverflow.com/questions/4950627/django-how-to-add-an-extra-form-to-a-formset-after-it-has-been-constructed"""
# def new_chararacter(request):
#     initialized_form = CharmForm(request.POST or None)
#     context = {'form': initialized_form,
#                'title': 'Describe a Charm with Traits'}
#     return new_form(request, initialized_form, context)
#
#
# def edit_character(request, primary_key):
#     model = get_object_or_404(Charm, pk=primary_key)
#     initialized_form = CharmForm(request.POST or None, instance=model)
#     if initialized_form.is_valid() and request.method == 'POST':
#         initialized_form.save()  # write instance updates to database
#     context = {'form': initialized_form,
#                'title': "Edit an Existing Charm"}
#     return render(request, 'Charms/new.html', context)

