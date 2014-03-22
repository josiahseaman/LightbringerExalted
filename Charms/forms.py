"""As a style note, we're going for big and round buttons.  You should be able to use the UI with your fist."""
__author__ = 'Josiah Seaman'
from crispy_forms.helper import FormHelper
from floppyforms import ModelForm, Select, SelectMultiple, CheckboxSelectMultiple
from Charms.models import Charm
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from crispy_forms.bootstrap import InlineRadios, Accordion, AccordionGroup, InlineCheckboxes


class ButtonArray(InlineRadios):
    def __init__(self, field_name,):
        return super(InlineRadios, self).__init__(field_name, template='floppyforms/radioselect_inline.html',)


# attrs = {'button0': "btn btn-default",
#          'button1': "btn btn-primary",
#          'button2': "btn btn-success",
#          'button3': "btn btn-info",
#          'button-1': "btn btn-warning",
#          'button-2': "btn btn-danger"}

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
            ButtonArray('scope_power'),
            ButtonArray('duration'),
            ButtonArray('magnitude'),
            ButtonArray('dice_bonus'),
            ButtonArray('negation'),
            Field('negation_detail', data_toggle_controller='negation', data_disabled_value='0'),
            ButtonArray('unnatural_mental_influence'),
            InlineRadios('extra_willpower_to_resist',
                         data_toggle_controller='unnatural_mental_influence',
                         data_disabled_value='0'),
            ButtonArray('speed_boost'),
            Accordion(
                AccordionGroup('Other Traits',
                    ButtonArray('weakness'),
                    Field('weakness_detail', data_toggle_controller='weakness', data_disabled_value='0'),
                    ButtonArray('narrative_benefit'),
                    ButtonArray('ally_buff'),
                    ButtonArray('counterattack'),
                    InlineCheckboxes('keywords'),
                    css_class='collapse'
            )),
            ButtonHolder(Submit('submit', 'Submit', css_class='button white'))
        )
        return super(self.__class__, self).__init__(*args, **kwargs)
    class Meta:
        model = Charm
        excluded = []