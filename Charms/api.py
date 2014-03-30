from tastypie.resources import ModelResource
from Charms.models import Charm


class CharmResource(ModelResource):
    class Meta:
        queryset = Charm.objects.all()
        resource_name = 'charm'