__author__ = 'Josiah Seaman'
from floppyforms import ModelForm, Select
from Charms.models import Charm


class Button_Array(Select):
    template_name = 'floppyforms/button_array.html'


class CharmForm(ModelForm):
    class Meta:
        model = Charm
        excluded = []
        widgets = {
            'scope_power': Button_Array(),
            'duration': Button_Array(),
            'magnitude': Button_Array(),
            'dice_bonus': Button_Array(),
            'ally_buff': Button_Array(),
            'negation': Button_Array(),
            'unnatural_mental_influence': Button_Array(),
            'extra_willpower_to_resist': Button_Array(),
            'weakness': Button_Array(),
            'narrative_benefit': Button_Array(),
            'counterattack': Button_Array(),
        }