# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Charm', fields ['name']
        db.delete_unique('Charms_charm', ['name'])


    def backwards(self, orm):
        # Adding unique constraint on 'Charm', fields ['name']
        db.create_unique('Charms_charm', ['name'])


    models = {
        'Charms.charm': {
            'Meta': {'object_name': 'Charm'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ally_buff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'applicability': ('django.db.models.fields.TextField', [], {}),
            'character_type': ('django.db.models.fields.CharField', [], {'default': "'Solar'", 'max_length': '255'}),
            'dice_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extra_willpower_to_resist': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'additional_willpower_purchases'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'narrative_benefit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'narrowness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation_detail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'speed_boost': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'unnatural_mental_influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weakness': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Charms']