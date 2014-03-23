from django.db import models
from Character.parsers import AnathemaParser

def statField():
    return models.IntegerField(default=0)

class LightbringerCharacter(models.Model):
    _source_character_sheet = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="Unnamed")  # May need to be extended for Deathknights
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

    @classmethod
    def create(cls, _source_filename=None):
        c = cls(_source_character_sheet=_source_filename)
        name = "Unnamed"
        if '.ecg' in _source_filename:
            parser = AnathemaParser(_source_filename)
            characterDict = parser.parse_to_dictionary()
            # c.name = characterSheet['Name']
        else:
            print("I don't know how to parse this file.")
            c.characterSheet = {}
        c = c.populate_fields(characterDict)
        return c

    def populate_fields(self, characterDict):
        for key in characterDict:
            try:
                self._meta.fields[key.lower()] = characterDict[key]
            except:
                print("No match found for: ", key)
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