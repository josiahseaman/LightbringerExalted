from django.db import models
from Character.glossary import ability_list


def doubleChoices(*args):
    return tuple([(x,x) for x in args])

def choiceList(*args):
    return tuple(enumerate(args))



class Charm(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)
    ability = models.CharField(max_length=15,
        choices=doubleChoices(*ability_list))
    character_type = models.CharField(max_length=255, default='Solar', choices=(('Solar', 'Solar'), ))
    applicability = models.TextField()
    duration = models.IntegerField(default=0, choices=choiceList('Instant', '5 activations', 'Scene or Dramatic Action', 'Permanent'))
    magnitude = models.IntegerField(default=0, choices=choiceList('Single', '5 targets', 'Magnitude 3', 'Nation', 'Direction'))
    dice_bonus = models.IntegerField(default=0, choices=choiceList('None', 'Augment (+3 dice)', 'Success Doubler', 'Perfect (Specialty)', 'Perfect (Ability)'))
    negation = models.IntegerField(default=0, choices=choiceList('None', 'Negate Penalties', 'Negate Requirement', 'Negate Normal Defense'))
    negation_detail = models.CharField(max_length=255, blank=True)
    speed_boost = models.CharField(max_length=255, blank=True,
                                   default='', choices=doubleChoices('Simple -> Reflexive', 'Dramatic Action -> Simple', 'Days -> Dramatic Action', 'Months -> Days'))
    unnatural_mental_influence = models.IntegerField(default=0,
                                                     choices=choiceList('None', 'Compulsion: Target resists w/ 1WP',
                                                                        'Intimacy: Target resists w/ 3WP (1wp to activate)',
                                                                        'Servitude Target resists w/ 5WP (2wp to activate)'))
    extra_willpower_to_resist = models.IntegerField(default=0, choices=choiceList('0 WP', '+2 WP (1wp to activate)', '+4 WP (2wp to activate)'),
                                                    db_column='additional_willpower_purchases')
    #other traits
    narrowness = models.IntegerField(default=0, choices=((0, 'Specialty'), (-1,'Trick'), (-2, 'Once per Arc')))
    weakness = models.IntegerField(default=0, choices=((0, 'None'),
                                                       (-1, 'Charm Requirement is easy to Byapss or Hard to Invoke  (Easily Overlooked, Counter Attacks)'),
                                                       (-2, 'Charm constrains the characters Available Actions (Bloodthirsty Sword Dancer)')))
    narrative_benefit = models.IntegerField(default=0, choices=choiceList(0, 1, 2),
                                            help_text="modifiers that don't fit within the usual system (Ghost-Eating)")
    ally_buff = models.IntegerField(default=0, choices=choiceList('Self', 'Ally gets Charm Benefits', 'Gain Supernatural Powers'))
    keywords = models.CharField(max_length=255, default='', blank=True, null=True,
                                choices=doubleChoices('Crippling', 'Form-type', 'Holy', 'Knockback',
                                                       'Obvious', 'Peircing', 'Poison', 'Shaping', 'Sickness',
                                                        'Surprise', 'Touch', 'Training'))

    def __str__(self):
        return "%s: %s.  %s" % (self.name, self.applicability, self.pretty_active_traits())

    def active_traits(self):
        traits_used = {}
        for field_name in ['duration', 'magnitude', 'dice_bonus', 'negation', 'speed_boost',
                           'unnatural_mental_influence', 'narrative_benefit', 'ally_buff', 'keywords']:
            value = self.__dict__[field_name]
            if value:  #This trait is used
                traits_used[field_name] = value
        return traits_used

    def pretty_active_traits(self):
        d = self.active_traits()
        representations = ["%s: %s" %(k, v) for k, v in d.items()]
        return ", ".join(representations)
