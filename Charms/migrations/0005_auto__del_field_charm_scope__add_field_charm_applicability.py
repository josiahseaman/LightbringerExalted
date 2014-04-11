# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Charm.scope'
        db.rename_column('Charms_charm', 'scope', 'applicability')
        db.delete_column('Charms_charm', 'scope_power')
        db.add_column('Charms_charm', 'narrowness', models.TextField(default=0))


    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration. 'Charm.scope' and its values cannot be restored.")

    models = {
        'Charms.charm': {
            'Meta': {'object_name': 'Charm'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ally_buff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'applicability': ('django.db.models.fields.TextField', [], {}),
            'character_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Solar'"}),
            'dice_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extra_willpower_to_resist': ('django.db.models.fields.IntegerField', [], {'db_column': "'additional_willpower_purchases'", 'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True', 'default': "''"}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'default': "''"}),
            'narrative_benefit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'narrowness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation_detail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'speed_boost': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'default': "''"}),
            'unnatural_mental_influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weakness': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Charms']