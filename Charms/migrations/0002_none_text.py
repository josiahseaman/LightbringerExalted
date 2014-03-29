# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for charm in orm.Charm.objects.all():
            if charm.speed_boost == 'None':
                charm.speed_boost = ''
                charm.save()


    def backwards(self, orm):
        raise RuntimeError("No reverse available")

    models = {
        'Charms.charm': {
            'Meta': {'object_name': 'Charm'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ally_buff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character_type': ('django.db.models.fields.CharField', [], {'default': "'Solar'", 'max_length': '255'}),
            'counterattack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dice_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extra_willpower_to_resist': ('django.db.models.fields.IntegerField', [], {'db_column': "'additional_willpower_purchases'", 'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'default': "''", 'max_length': '255'}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'default': "''", 'max_length': '255'}),
            'narrative_benefit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation_detail': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'scope': ('django.db.models.fields.TextField', [], {}),
            'scope_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_boost': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'unnatural_mental_influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weakness': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Charms']
    symmetrical = True
