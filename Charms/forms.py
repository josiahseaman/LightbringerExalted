"""As a style note, we're going for big and round buttons.  You should be able to use the UI with your fist."""
__author__ = 'Josiah Seaman'
from crispy_forms.helper import FormHelper
from floppyforms import ModelForm, Select
from Charms.models import Charm
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import InlineRadios, Accordion, AccordionGroup


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
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'ability',
            'scope',
            InlineRadios('scope_power'),
            InlineRadios('duration'),
            InlineRadios('magnitude'),
            InlineRadios('dice_bonus'),
            InlineRadios('negation'),
            Field('negation_detail', data_toggle_controller='negation', data_disabled_value='0'),
            InlineRadios('unnatural_mental_influence'),
            InlineRadios('extra_willpower_to_resist',
                         data_toggle_controller='unnatural_mental_influence',
                         data_disabled_value='0'),
            InlineRadios('speed_boost'),
            Accordion(
                AccordionGroup('Other Traits',
                    InlineRadios('weakness'),
                    InlineRadios('narrative_benefit'),
                    InlineRadios('ally_buff'),
                    InlineRadios('counterattack'),
                    css_class='collapse'
            )),
            ButtonHolder(Submit('submit', 'Submit', css_class='button white'))
        )
        return super(self.__class__, self).__init__(*args, **kwargs)
    class Meta:
        model = Charm
        excluded = []