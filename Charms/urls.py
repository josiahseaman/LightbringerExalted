__author__ = 'Josiah'
from django.conf.urls import patterns, url  # do not delete this

urlpatterns = patterns('',
                       url(r'^Charm/new/$', 'Charms.views.new_charm'),
                       url(r'^Charm/(?P<primary_key>\d+)/$', 'Charms.views.edit_charm'),
                       url(r'^Charm/(?P<primary_key>\d+)/copy/$', 'Charms.views.copy_charm'),

)