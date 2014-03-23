from django.db import models


class LightbringerCharacter(models.Model):
    _source_character_sheet = models.CharField(max_length=255)

    @classmethod
    def create(cls, _source_character_sheet):
        parsedCharacter = cls(_source_character_sheet=_source_character_sheet)
        # do something with the book
        return parsedCharacter

