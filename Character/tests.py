from django.test import TestCase
import unittest
from Character import glossary
from Character.models import LightbringerCharacter


class CharacterTest(unittest.TestCase):
    # Change to a TransactionTestCase
    from Character.models import LightbringerCharacter
    c = LightbringerCharacter.create('Willow.ecg')
    blankC = LightbringerCharacter()

    def testAbilityCreation(self):
        self.blankC.create_ability_list()
        self.assertEqual(self.blankC, self.blankC.Larceny.character)
        for ability in glossary.ability_list:
            self.assertTrue(ability in self.blankC.__dict__.keys, ability + " not attached to character sheet")

    def test_set_stat(self):
        self.blankC.set_stat('Stealth', character_dict={'Stealth':4, str(glossary.specialties):{'Stealth':('Corners',2)}})
        self.assertEqual(self.blankC.Stealth.dots, 4)
        self.assertEqual(self.blankC.Stealth.specialties.objects.all()[0].dots, 2)

    def testAttributeValues(self):
        values = [int(self.c.getStat(stat)) for stat in ['Charisma', 'Presence', 'Survival']]
        self.assertListEqual(values, [5, 3, 5])
        self.assertRaises(KeyError, self.c.getStat, 'Computers')
        self.assertEqual(self.c.sumDicePool('Perception', 'Awareness'), 8)

    def testStringValues(self):
        self.assertEqual(self.c.name, 'Willow')

    def testSaveToDB(self):
        self.c.save()
        dbc = LightbringerCharacter.objects.filter(name='Willow')[0]
        values = [int(dbc.getStat(stat)) for stat in ['Charisma', 'Presence', 'Survival']]
        self.assertListEqual(values, [5, 3, 5])
        print(dbc.equipment, type(dbc.equipment))

    def testCreateSpecialty(self):
        self.c.save()
        dbc = LightbringerCharacter.objects.filter(name='Willow')[0]
        print(dbc.specialties.all())

class AnathemaParserTest(unittest.TestCase):
    from Character.parsers import AnathemaParser
    ap = AnathemaParser('Willow.ecg')
    root = ap.root

    def testParse(self):
        result = self.ap.parse_to_dictionary()
        expected = {'Appearance': 4,
                    'Archery': 0,
                    'Athletics': 3,
                    'Awareness': 5,
                    'Bureaucracy': 0,
                    'Charisma': 5,
                    'Compassion': 2,
                    'Concept': 'Druid Sorceror',
                    'Conviction': 3,
                    'Craft': 0,
                    'Dexterity': 3,
                    'Dodge': 5,
                    'Equipment': ['Superheavy Plate (Artifact)',
                                  'Wood Dragon Claw (Offensive)',
                                  'Wood Dragon Claw (Defensive)'],
                    'Essence': 4,
                    'Integrity': 0,
                    'Intelligence': 4,
                    'Investigation': 0,
                    'Larceny': 0,
                    'Limit': 0,
                    'Linguistics': 0,
                    'Lore': 2,
                    'Manipulation': 2,
                    'MartialArts': 5,
                    'Medicine': 0,
                    'Melee': 0,
                    'Name': 'Willow',
                    'Occult': 5,
                    'Perception': 3,
                    'Performance': 1,
                    'Player': 'Corina',
                    'Presence': 3,
                    'Resistance': 1,
                    'Ride': 1,
                    'Sail': 0,
                    'Socialize': 1,
                    'Specialties': {'Occult': ('Forest', 3), 'Survival': ('Leading Groups', 1)},
                    'Stamina': 2,
                    'Stealth': 2,
                    'Strength': 2,
                    'Survival': 5,
                    'Temperance': 2,
                    'Thrown': 0,
                    'Type': 'Solar',
                    'Valor': 2,
                    'War': 0,
                    'Willpower': 7,
                    'Wits': 2}
        self.assertDictEqual(result, expected, )



if __name__ == '__main__':
    unittest.main()
