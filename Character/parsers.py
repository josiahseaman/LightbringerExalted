__author__ = 'Josiah Seaman'
from xml.etree.ElementTree import ElementTree
from Character.glossary import *


class AnathemaParser:
    def __init__(self, filename):
        tree = ElementTree(file='characters/' + filename)
        self.root = tree.getroot()
        self.sheet = {}

    def parse_to_dictionary(self):
        self.parse_text_fields()
        self.parse_numeric_fields()
        self.parse_lists()
        return self.sheet

    def parse_text_fields(self):
        text_fields = [('Name', 'CharacterName'), 'Player', 'Concept', ('Type', 'CharacterType'), ]
        for t in text_fields:
            if isinstance(t, tuple):
                self.populate_text_field(*t)
            else:
                self.populate_text_field(t)

    def parse_numeric_fields(self):
        self.sheet[specialties] = {}
        numeric_fields = [essence, willpower, compassion, conviction, temperance, valor, strength, dexterity, dex,
                          stamina, charisma, manipulation, appearance, perception, intelligence, wits, craft, archery,
                          martialarts, melee, thrown, war, integrity, performance, presence, resistance, survival,
                          investigation, lore, medicine, occult, athletics, awareness, dodge, larceny, stealth,
                          bureaucracy, linguistics, ride, sail, socialize, limit, ]
        for x in numeric_fields:
            self.populate_numeric_field(x)

    def parse_lists(self):
        lists = ['Spells', 'Combos', 'Charms', 'Backgrounds']
        additional_models = ['Mutations', 'Intimacies', 'SolarVirtueFlaw', ]  # 'Equipment',
        # TODO: 'Craft', 'Linguistics' needs special care to get the right one
        self.sheet['Equipment'] = self.gearList()

    def populate_text_field(self, field_name, anathema_name = ''):
        if not anathema_name:
            anathema_name = field_name
        text = ''
        try:
            element = next(self.root.iter(anathema_name))
            text = self.getText(element)
        except: pass
        self.sheet[field_name] = text

    def populate_numeric_field(self, field_name):
        self.sheet[field_name] = self.getStat(field_name)
        if self.getSpecialty(field_name):
            self.sheet['Specialties'][field_name] = self.getSpecialty(field_name)

    def getStatNumber(self, element):
        result = element.get('experiencedValue', None)
        if not result:
            result = element.get('creationValue', None)
        return int(result or 0)

    def getSpecialty(self, statName):
        """Check for specialties, assumes they are applicable to this roll."""
        try:
            element = next(self.root.iter(statName))
            specialtyElem = next(element.iter('Specialty'))  # TODO: assumes you only have one specialty per skill
            return specialtyElem.attrib['name'], self.getStatNumber(specialtyElem)
        except:
            return None

    def getStat(self, statName):
        statName = statName.lower().capitalize()  #proper capitalization
        # try: return self.magicalEffects[statName]
        # except: pass
        if statName == 'Martialarts':
            statName = 'MartialArts'
        try:
            element = next(self.root.iter(statName))
        except:
            raise KeyError(str(statName) + ": No such stat")
        if statName == 'Craft':
            branches = element.getiterator('subTrait')
            result = max(list(map(self.getStatNumber, branches)))
        else:
            result = self.getStatNumber(element)
        return result

    def gearList(self):
        models = self.additionalModels()
        gearNames = []
        for i in range(1, 20):  # try grabbing a gear name
            try:
                gearNames.append(next(models['Equipment'][0][i][0].itertext()))
            except:
                pass
        return gearNames

    def additionalModels(self):
        e = next(self.root.getiterator('AdditionalModels'))
        availableModels = {x.get('templateId'): x for x in e.getchildren()}
        return availableModels

    def getText(self, elem):
        return ",".join(elem.itertext())
