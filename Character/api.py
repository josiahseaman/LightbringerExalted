from tastypie import fields
from tastypie.resources import ModelResource
from Character.models import Specialty, LightbringerCharacter


class LightbringerCharacterResource(ModelResource):
    specialties = fields.ToManyField('Character.api.SpecialtyResource', 'specialties')
    class Meta:
        queryset = LightbringerCharacter.objects.all()
        resource_name = 'character'

class SpecialtyResource(ModelResource):
    character = fields.ToOneField(LightbringerCharacterResource, '_character')
    class Meta:
        queryset = Specialty.objects.all()
        resource_name = 'specialty'
