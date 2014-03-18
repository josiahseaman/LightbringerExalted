__author__ = 'Josiah Seaman'
from floppyforms import ModelForm, Select
from Charms.models import Charm


class Button_Array(Select):
    template_name = 'floppyforms/button_array.html'
    attrs = {0: "btn btn-default",
             1: "btn btn-primary",
             2: "btn btn-success",
             3: "btn btn-info",
             -1: "btn btn-warning",
             -2: "btn btn-danger"}


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
            'speed_boost': Button_Array(),
            'unnatural_mental_influence': Button_Array(),
            'extra_willpower_to_resist': Button_Array(),
            'weakness': Button_Array(),
            'narrative_benefit': Button_Array(),
            'counterattack': Button_Array(),
        }