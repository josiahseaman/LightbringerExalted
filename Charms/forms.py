from crispy_forms.helper import FormHelper

__author__ = 'Josiah Seaman'
from floppyforms import ModelForm, Select
from Charms.models import Charm
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineRadios


class Button_Array(Select):
    template_name = 'floppyforms/button_array.html'
    attrs = {0: "btn btn-default",
             1: "btn btn-primary",
             2: "btn btn-success",
             3: "btn btn-info",
             -1: "btn btn-warning",
             -2: "btn btn-danger"}


class CharmForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'ability',
            'scope',
            InlineRadios('scope_power'),
            InlineRadios('duration'),
            InlineRadios('magnitude'),
            InlineRadios('dice_bonus'),
            InlineRadios('negation'),
            'negation_detail',
            InlineRadios('speed_boost'),
            InlineRadios('unnatural_mental_influence'),
            InlineRadios('extra_willpower_to_resist'),
            #Other traits
            InlineRadios('weakness'),
            InlineRadios('narrative_benefit'),
            InlineRadios('ally_buff'),
            InlineRadios('counterattack'),
            ButtonHolder(Submit('submit', 'Submit', css_class='button white'))
        )
        return super(self.__class__, self).__init__(*args, **kwargs)
    class Meta:
        model = Charm
        excluded = []