# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ability'
        db.create_table('Character_ability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('Character', ['Ability'])

        # Adding model 'CharacterAbility'
        db.create_table('Character_characterability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.Ability'])),
            ('dots', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mastery', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('character', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.LightbringerCharacter'])),
        ))
        db.send_create_signal('Character', ['CharacterAbility'])

        # Deleting field 'Specialty._character'
        db.delete_column('Character_specialty', '_character_id')


        # Renaming column for 'Specialty.ability' to match new field type.
        db.rename_column('Character_specialty', 'ability', 'ability_id')
        # Changing field 'Specialty.ability'
        db.alter_column('Character_specialty', 'ability_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.CharacterAbility']))
        # Adding index on 'Specialty', fields ['ability']
        db.create_index('Character_specialty', ['ability_id'])

        # Deleting field 'LightbringerCharacter.dodge'
        db.delete_column('Character_lightbringercharacter', 'dodge')

        # Deleting field 'LightbringerCharacter.larceny'
        db.delete_column('Character_lightbringercharacter', 'larceny')

        # Deleting field 'LightbringerCharacter.athletics'
        db.delete_column('Character_lightbringercharacter', 'athletics')

        # Deleting field 'LightbringerCharacter.craft'
        db.delete_column('Character_lightbringercharacter', 'craft')

        # Deleting field 'LightbringerCharacter.lore'
        db.delete_column('Character_lightbringercharacter', 'lore')

        # Deleting field 'LightbringerCharacter.awareness'
        db.delete_column('Character_lightbringercharacter', 'awareness')

        # Deleting field 'LightbringerCharacter.presence'
        db.delete_column('Character_lightbringercharacter', 'presence')

        # Deleting field 'LightbringerCharacter.socialize'
        db.delete_column('Character_lightbringercharacter', 'socialize')

        # Deleting field 'LightbringerCharacter.integrity'
        db.delete_column('Character_lightbringercharacter', 'integrity')

        # Deleting field 'LightbringerCharacter.archery'
        db.delete_column('Character_lightbringercharacter', 'archery')

        # Deleting field 'LightbringerCharacter.medicine'
        db.delete_column('Character_lightbringercharacter', 'medicine')

        # Deleting field 'LightbringerCharacter.performance'
        db.delete_column('Character_lightbringercharacter', 'performance')

        # Deleting field 'LightbringerCharacter.war'
        db.delete_column('Character_lightbringercharacter', 'war')

        # Deleting field 'LightbringerCharacter.linguistics'
        db.delete_column('Character_lightbringercharacter', 'linguistics')

        # Deleting field 'LightbringerCharacter.investigation'
        db.delete_column('Character_lightbringercharacter', 'investigation')

        # Deleting field 'LightbringerCharacter.resistance'
        db.delete_column('Character_lightbringercharacter', 'resistance')

        # Deleting field 'LightbringerCharacter.occult'
        db.delete_column('Character_lightbringercharacter', 'occult')

        # Deleting field 'LightbringerCharacter.bureaucracy'
        db.delete_column('Character_lightbringercharacter', 'bureaucracy')

        # Deleting field 'LightbringerCharacter.stealth'
        db.delete_column('Character_lightbringercharacter', 'stealth')

        # Deleting field 'LightbringerCharacter.martialarts'
        db.delete_column('Character_lightbringercharacter', 'martialarts')

        # Deleting field 'LightbringerCharacter.melee'
        db.delete_column('Character_lightbringercharacter', 'melee')

        # Deleting field 'LightbringerCharacter.ride'
        db.delete_column('Character_lightbringercharacter', 'ride')

        # Deleting field 'LightbringerCharacter.survival'
        db.delete_column('Character_lightbringercharacter', 'survival')

        # Deleting field 'LightbringerCharacter.thrown'
        db.delete_column('Character_lightbringercharacter', 'thrown')

        # Deleting field 'LightbringerCharacter.sail'
        db.delete_column('Character_lightbringercharacter', 'sail')


    def backwards(self, orm):
        # Removing index on 'Specialty', fields ['ability']
        db.delete_index('Character_specialty', ['ability_id'])

        # Deleting model 'Ability'
        db.delete_table('Character_ability')

        # Deleting model 'CharacterAbility'
        db.delete_table('Character_characterability')


        # User chose to not deal with backwards NULL issues for 'Specialty._character'
        raise RuntimeError("Cannot reverse this migration. 'Specialty._character' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Specialty._character'
        db.add_column('Character_specialty', '_character',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Character.LightbringerCharacter'], related_name='specialties'),
                      keep_default=False)


        # Renaming column for 'Specialty.ability' to match new field type.
        db.rename_column('Character_specialty', 'ability_id', 'ability')
        # Changing field 'Specialty.ability'
        db.alter_column('Character_specialty', 'ability', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Adding field 'LightbringerCharacter.dodge'
        db.add_column('Character_lightbringercharacter', 'dodge',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.larceny'
        db.add_column('Character_lightbringercharacter', 'larceny',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.athletics'
        db.add_column('Character_lightbringercharacter', 'athletics',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.craft'
        db.add_column('Character_lightbringercharacter', 'craft',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.lore'
        db.add_column('Character_lightbringercharacter', 'lore',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.awareness'
        db.add_column('Character_lightbringercharacter', 'awareness',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.presence'
        db.add_column('Character_lightbringercharacter', 'presence',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.socialize'
        db.add_column('Character_lightbringercharacter', 'socialize',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.integrity'
        db.add_column('Character_lightbringercharacter', 'integrity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.archery'
        db.add_column('Character_lightbringercharacter', 'archery',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.medicine'
        db.add_column('Character_lightbringercharacter', 'medicine',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.performance'
        db.add_column('Character_lightbringercharacter', 'performance',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.war'
        db.add_column('Character_lightbringercharacter', 'war',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.linguistics'
        db.add_column('Character_lightbringercharacter', 'linguistics',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.investigation'
        db.add_column('Character_lightbringercharacter', 'investigation',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.resistance'
        db.add_column('Character_lightbringercharacter', 'resistance',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.occult'
        db.add_column('Character_lightbringercharacter', 'occult',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.bureaucracy'
        db.add_column('Character_lightbringercharacter', 'bureaucracy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.stealth'
        db.add_column('Character_lightbringercharacter', 'stealth',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.martialarts'
        db.add_column('Character_lightbringercharacter', 'martialarts',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.melee'
        db.add_column('Character_lightbringercharacter', 'melee',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.ride'
        db.add_column('Character_lightbringercharacter', 'ride',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.survival'
        db.add_column('Character_lightbringercharacter', 'survival',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.thrown'
        db.add_column('Character_lightbringercharacter', 'thrown',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'LightbringerCharacter.sail'
        db.add_column('Character_lightbringercharacter', 'sail',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Character.LightbringerCharacter']"}),
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
            'concept': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
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
            'player': ('django.db.models.fields.CharField', [], {'default': "'NPC'", 'max_length': '255'}),
            'spells': ('django.db.models.fields.TextField', [], {}),
            'stamina': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'temperance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'Solar'", 'max_length': '255'}),
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