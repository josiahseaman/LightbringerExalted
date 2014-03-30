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
    character = models.ForeignKey('LightbringerCharacter', related_name='abilities')
    def __str__(self):
        return "%s: %i" % (self.ability, self.dots)


class Specialty(models.Model):
    ability = models.ForeignKey(CharacterAbility, related_name='specialties')
    focus_area = models.CharField(max_length=255, )
    dots = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    def __str__(self):
        return "%s (%s) %i" % (self.ability, self.focus_area, self.dots)


def create_specialties(dictionary, character):
    for key, value in dictionary.items():
        s = Specialty(ability=key, focus_area=value[0], dots=value[1], _character=character)
        s.save()
        print(s)
    print("Created %i Specialties for %s" % (len(dictionary), character.name))


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
    # Abilities
    archery = statField()
    martialarts = statField()
    melee = statField()
    thrown = statField()
    war = statField()
    integrity = statField()
    performance = statField()
    presence = statField()
    resistance = statField()
    survival = statField()
    craft = statField()
    investigation = statField()
    lore = statField()
    medicine = statField()
    occult = statField()
    athletics = statField()
    awareness = statField()
    dodge = statField()
    larceny = statField()
    stealth = statField()
    bureaucracy = statField()
    linguistics = statField()
    ride = statField()
    sail = statField()
    socialize = statField()
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
        else:
            raise IOError("I don't know how to parse this file.")
        c = c.populate_fields(character_dict)
        c.save()
        create_specialties(character_dict[glossary.specialties], c)
        return c

    def populate_fields(self, character_dict):
        for key in character_dict:
            try:
                setattr(self, key.lower(), character_dict[key])
            except:
                print("No match found for: ", key)
        print(self.equipment)
        return self

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