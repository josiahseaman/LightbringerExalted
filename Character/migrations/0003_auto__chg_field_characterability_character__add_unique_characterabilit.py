# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CharacterAbility.character'
        db.alter_column('Character_characterability', 'character_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['Character.LightbringerCharacter']))
        # Adding unique constraint on 'CharacterAbility', fields ['character']
        db.create_unique('Character_characterability', ['character_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'CharacterAbility', fields ['character']
        db.delete_unique('Character_characterability', ['character_id'])


        # Changing field 'CharacterAbility.character'
        db.alter_column('Character_characterability', 'character_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.LightbringerCharacter']))

    models = {
        'Character.ability': {
            'Meta': {'object_name': 'Ability'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Character.characterability': {
            'Meta': {'object_name': 'CharacterAbility'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Character.Ability']"}),
            'character': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['Character.LightbringerCharacter']", 'related_name': "'Larceny'"}),
            'dots': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mastery': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'Character.lightbringercharacter': {
            'Meta': {'object_name': 'LightbringerCharacter'},
            '_source_character_sheet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'appearance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'backgrounds': ('django.db.models.fields.TextField', [], {}),
            'charisma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charms': ('django.db.models.fields.TextField', [], {}),
            'combos': ('django.db.models.fields.TextField', [], {}),
            'compassion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'concept': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'conviction': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'equipment': ('django.db.models.fields.TextField', [], {}),
            'essence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelligence': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'intimacies': ('django.db.models.fields.TextField', [], {}),
            'languages': ('django.db.models.fields.TextField', [], {}),
            'limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'manipulation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mutations': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'perception': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'NPC'"}),
            'spells': ('django.db.models.fields.TextField', [], {}),
            'stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'temperance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "'Solar'"}),
            'valor': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'virtue_flaw': ('django.db.models.fields.TextField', [], {}),
            'willpower': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'wits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'Character.specialty': {
            'Meta': {'object_name': 'Specialty'},
            'ability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Character.CharacterAbility']", 'related_name': "'specialties'"}),
            'dots': ('django.db.models.fields.IntegerField', [], {}),
            'focus_area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Character']