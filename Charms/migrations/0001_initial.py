# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Charm'
        db.create_table('Charms_charm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, default='')),
            ('ability', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('character_type', self.gf('django.db.models.fields.CharField')(max_length=255, default='Solar')),
            ('scope', self.gf('django.db.models.fields.TextField')()),
            ('scope_power', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('duration', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('magnitude', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dice_bonus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('negation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('negation_detail', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=255)),
            ('speed_boost', self.gf('django.db.models.fields.CharField')(max_length=255, default='None')),
            ('unnatural_mental_influence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('extra_willpower_to_resist', self.gf('django.db.models.fields.IntegerField')(db_column='additional_willpower_purchases', default=0)),
            ('weakness', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('narrative_benefit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ally_buff', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('counterattack', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('keywords', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=255, default='')),
        ))
        db.send_create_signal('Charms', ['Charm'])


    def backwards(self, orm):
        # Deleting model 'Charm'
        db.delete_table('Charms_charm')


    models = {
        'Charms.charm': {
            'Meta': {'object_name': 'Charm'},
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ally_buff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Solar'"}),
            'counterattack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dice_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extra_willpower_to_resist': ('django.db.models.fields.IntegerField', [], {'db_column': "'additional_willpower_purchases'", 'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255', 'default': "''"}),
            'magnitude': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'default': "''"}),
            'narrative_benefit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'negation_detail': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'scope': ('django.db.models.fields.TextField', [], {}),
            'scope_power': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'speed_boost': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'None'"}),
            'unnatural_mental_influence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weakness': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['Charms']