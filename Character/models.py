from django.db import models
from Character.parsers import AnathemaParser


class LightbringerCharacter(models.Model):
    _source_character_sheet = models.CharField(max_length=255)

    @classmethod
    def add_fields_by_dictionary(cls, instance, characterDict):
        for key in characterDict:  # Add dict as fields
            v = characterDict[key]
            if isinstance(v, int):
                field = models.IntegerField(default=characterDict[key])
            elif isinstance(v, str):
                field = models.CharField(max_length=255, default=characterDict[key])
            elif isinstance(v, (dict, list)):
                field = None  # TODO: handle dict and list
            else:
                raise ValueError("Unrecognized type in character dictionary %s: %s" % (str(key), str(v)))
                # field = models.TextField(blank=True, null=True)
            if field is not None:
                cls.add_to_class(str(key).lower(), field)

    @classmethod
    def create(cls, _source_filename=None):
        c = cls(_source_character_sheet=_source_filename)
        name = "Unnamed"
        if '.ecg' in _source_filename:
            parser = AnathemaParser(_source_filename)
            characterSheet = parser.parse_to_dictionary()
            # c.name = characterSheet['Name']
        else:
            print("I don't know how to parse this file.")
            c.characterSheet = {}

        cls.add_fields_by_dictionary(c, characterSheet)

        return c

