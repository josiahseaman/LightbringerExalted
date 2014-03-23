from django.test import TestCase
import unittest

class CharacterTest(unittest.TestCase):
    from Character.models import LightbringerCharacter
    c = LightbringerCharacter.create('Willow.ecg')

    def testPrintAttributes(self):
        print(self.c.name)
        usefulStats = ['Charisma', 'Presence', 'Survival']

        for stat in usefulStats:
            print(stat, ":", int(self.c.getStat(stat) or 0))
        self.assertRaises(KeyError, self.c.getStat, 'Computers')
        print("For 'Perception', 'Awareness' Roll", self.c.sumDicePool('Perception', 'Awareness'), "dice")



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
