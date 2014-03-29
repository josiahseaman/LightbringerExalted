# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialty'
        db.create_table('Character_specialty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ability', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('focus_area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dots', self.gf('django.db.models.fields.IntegerField')()),
            ('_character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.LightbringerCharacter'], related_name='specialties')),
        ))
        db.send_create_signal('Character', ['Specialty'])

        # Adding model 'LightbringerCharacter'
        db.create_table('Character_lightbringercharacter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_source_character_sheet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('player', self.gf('django.db.models.fields.CharField')(max_length=255, default='NPC')),
            ('concept', self.gf('django.db.models.fields.CharField')(max_length=255, default='')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255, default='Solar')),
            ('strength', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dex', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('stamina', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('charisma', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('manipulation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('appearance', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('perception', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intelligence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wits', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('archery', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('martialarts', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('melee', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('thrown', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('war', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('integrity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('performance', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('presence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resistance', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('survival', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('craft', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('investigation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lore', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('medicine', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('occult', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('athletics', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('awareness', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dodge', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('larceny', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('stealth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('bureaucracy', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('linguistics', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ride', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sail', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('socialize', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('willpower', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('essence', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('limit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('compassion', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('conviction', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('temperance', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('valor', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intimacies', self.gf('django.db.models.fields.TextField')()),
            ('backgrounds', self.gf('django.db.models.fields.TextField')()),
            ('equipment', self.gf('django.db.models.fields.TextField')()),
            ('charms', self.gf('django.db.models.fields.TextField')()),
            ('combos', self.gf('django.db.models.fields.TextField')()),
            ('spells', self.gf('django.db.models.fields.TextField')()),
            ('virtue_flaw', self.gf('django.db.models.fields.TextField')()),
            ('mutations', self.gf('django.db.models.fields.TextField')()),
            ('languages', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('Character', ['LightbringerCharacter'])


    def backwards(self, orm):
        # Deleting model 'Specialty'
        db.delete_table('Character_specialty')

        # Deleting model 'LightbringerCharacter'
        db.delete_table('Character_lightbringercharacter')


    models = {
        'Character.lightbringercharacter': {
            'Meta': {'object_name': 'LightbringerCharacter'},
            '_source_character_sheet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'appearance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'archery': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'athletics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'awareness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'backgrounds': ('django.db.models.fields.TextField', [], {}),
            'bureaucracy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charisma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charms': ('django.db.models.fields.TextField', [], {}),
            'combos': ('django.db.models.fields.TextField', [], {}),
            'compassion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'concept': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'conviction': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'craft': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dodge': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'equipment': ('django.db.models.fields.TextField', [], {}),
            'essence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'integrity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intimacies': ('django.db.models.fields.TextField', [], {}),
            'investigation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'languages': ('django.db.models.fields.TextField', [], {}),
            'larceny': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'linguistics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lore': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'martialarts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'medicine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'melee': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mutations': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'occult': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'performance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'NPC'"}),
            'presence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'resistance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ride': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sail': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'socialize': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spells': ('django.db.models.fields.TextField', [], {}),
            'stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'stealth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'survival': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'temperance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thrown': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Solar'"}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'virtue_flaw': ('django.db.models.fields.TextField', [], {}),
            'war': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'willpower': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'Character.specialty': {
            'Meta': {'object_name': 'Specialty'},
            '_character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Character.LightbringerCharacter']", 'related_name': "'specialties'"}),
            'ability': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dots': ('django.db.models.fields.IntegerField', [], {}),
            'focus_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Character']