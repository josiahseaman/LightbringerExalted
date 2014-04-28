from django.conf.urls import patterns, include, url
from tastypie.api import Api
from Charms import urls
from django.contrib import admin
from Charms.api import CharmResource
from Character.api import LightbringerCharacterResource, SpecialtyResource
from views import everything

admin.autodiscover()
v1_0_api = Api(api_name='v1.0')
v1_0_api.register(CharmResource())
v1_0_api.register(LightbringerCharacterResource())
v1_0_api.register(SpecialtyResource())

urlpatterns = patterns('',
    url(r'^ajax/', include('ajax.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('Charms.urls')),
    # url(r'^', include('Character.urls')),
    url(r'^api/', include(v1_0_api.urls)),
    url(r'^charms', everything),
    url(r'^charm/.*', everything),
    # url(r'^.*', everything),
)
