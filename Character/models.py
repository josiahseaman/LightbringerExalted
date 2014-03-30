from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from Character import glossary
from Character.parsers import AnathemaParser
import Charms.models as CharmModels


def statField():
    return models.IntegerField(default=0)


class Ability(models.Model):
    name = models.CharField(max_length=50, )
    description = models.TextField()
    def __str__(self):
        return self.name


class CharacterAbility(models.Model):
    ability = models.ForeignKey(Ability)
    dots = models.IntegerField(default=0)
    mastery = models.IntegerField(default=0)
    character = models.ForeignKey('LightbringerCharacter', related_name=ability.name)
    def __str__(self):
        return "%s: %i" % (self.ability, self.dots)


class Specialty(models.Model):
    ability = models.ForeignKey(CharacterAbility, related_name='specialties')
    focus_area = models.CharField(max_length=255, )
    dots = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    def __str__(self):
        return "%s (%s) %i" % (self.ability, self.focus_area, self.dots)


class LightbringerCharacter(models.Model):
    _source_character_sheet = models.CharField(max_length=255)
    name = models.CharField(max_length=255, )  # May need to be extended for Deathknight names :)
    player = models.CharField(max_length=255, default='NPC')
    concept = models.CharField(max_length=255, default='')
    type = models.CharField(max_length=255, default='Solar')
    # Attributes
    strength = statField()
    dexterity = statField()
    dex = statField()
    stamina = statField()
    charisma = statField()
    manipulation = statField()
    appearance = statField()
    perception = statField()
    intelligence = statField()
    wits = statField()
    # Abilities are foreignkeyed

    # Other stats
    willpower = statField()
    essence = statField()
    limit = statField()
    compassion = statField()
    conviction = statField()
    temperance = statField()
    valor = statField()
    #specialties are ForeignKeyed in class Specialty
    # Complex fields
    intimacies = models.TextField()
    backgrounds = models.TextField()
    equipment = models.TextField()
    charms = models.TextField()
    combos = models.TextField()
    spells = models.TextField()
    virtue_flaw = models.TextField()
    mutations = models.TextField()
    #'Craft', 'Linguistics' needs special care to get the right one
    languages = models.TextField()

    def __str__(self):
        return "%s %i" % (self.name, self.id)

    @classmethod
    def create(cls, _source_filename=None):
        c = cls(_source_character_sheet=_source_filename)
        if '.ecg' in _source_filename:
            parser = AnathemaParser(_source_filename)
            character_dict = parser.parse_to_dictionary()
            c.save()
        else:
            raise IOError("I don't know how to parse this file.")
        c.create_ability_list()
        c = c.populate_fields(character_dict)
        return c

    def create_ability_list(self):
        abilities = Ability.objects.all()
        for skill in abilities:
            ca = CharacterAbility(ability=skill, character=self)
            # Need to set related name?

    def populate_fields(self, character_dict):
        for key in character_dict:
            try:
                setattr(self, key.lower(), character_dict[key])
            except:
                try:
                    self.set_stat(key, character_dict)
                except:
                    print("No match found for: ", key)
        print(self.equipment)
        return self

    def set_stat(self, stat_name, character_dict):
        dots = character_dict[stat_name]
        stat = self.__dict__[stat_name.lower()]
        stat.dots = dots
        stat.save()
        specialties = character_dict[glossary.specialties]
        if stat_name in specialties.keys():
            value = specialties[stat_name]
            s = Specialty(ability=stat, focus_area=value[0], dots=value[1])
            s.save()
            print(s)


    def getStat(self, statName):
        return self.__dict__[statName.lower()]
        # return self._meta.fields[statName.lower()]

    def __getitem__(self, item):
        return self.getStat(item)

    def sumDicePoolWithoutPenalties(self, *stats):
        dicePool = 0
        for stat in stats: #I can do this with reduce, but it's harder to read
            try:
                dicePool += self[stat]
            except AttributeError:
                dicePool += stat #this is probably a number
        return dicePool

    def sumDicePool(self, *stats):
        return self.sumDicePoolWithoutPenalties(*stats)