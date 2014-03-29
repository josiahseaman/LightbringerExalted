# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    # no_dry_run = True
    def forwards(self, orm):
        # Deleting field 'Charm.counterattack'
        # for charm in orm.Charm.objects.all():
        #     if charm.counterattack:
        #         charm.weakness += -1
        db.delete_column('Charms_charm', 'counterattack')


    def backwards(self, orm):
        # Adding field 'Charm.counterattack'
        db.add_column('Charms_charm', 'counterattack',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        'Charms.charm': {
            'Meta': {'object_name': 'Charm'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ally_buff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character_type': ('django.db.models.fields.CharField', [], {'default': "'Solar'", 'max_length': '255'}),
            'dice_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extra_willpower_to_resist': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_column': "'additional_willpower_purchases'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'unique': 'True'}),
            'narrative_benefit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation_detail': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'scope': ('django.db.models.fields.TextField', [], {}),
            'scope_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_boost': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'unnatural_mental_influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weakness': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Charms']