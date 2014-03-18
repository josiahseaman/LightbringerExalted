__author__ = 'Josiah Seaman'
from floppyforms import ModelForm
from Charms.models import Charm


class CharmForm(ModelForm):
    class Meta:
        model = Charm
