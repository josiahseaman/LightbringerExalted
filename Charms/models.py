from django.db import models

def doubleChoices(*args):
    return tuple([(x,x) for x in args])

def choiceList(*args):
    return tuple(enumerate(args))


class Charm(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)
    ability = models.CharField(max_length=15,
        choices=doubleChoices('Craft', 'Archery', 'MartialArts', 'Melee', 'Thrown', 'War', 'Integrity', 'Performance', 'Presence', 'Resistance', 'Survival', 'Investigation', 'Lore', 'Medicine', 'Occult', 'Athletics', 'Awareness', 'Dodge', 'Larceny', 'Stealth', 'Bureaucracy', 'Linguistics', 'Ride', 'Sail', 'Socialize'))
    scope = models.TextField()
    scope_power = models.IntegerField(default=0, choices=((-1,'Trick'), (0, 'Specialty'), (1, 'Ability'), (2, 'Caste Abilities')))
    duration = models.IntegerField(default=0, choices=choiceList('Instant', '5 activations', 'Scene or Dramatic Action', 'Permanent'))
    magnitude = models.IntegerField(default=0, choices=choiceList('Single', '5 targets', 'Magnitude 3', 'Nation', 'Direcion'))
    dice_bonus = models.IntegerField(default=0, choices=choiceList('None', 'Augment (+3 dice)', 'Success Doubler', 'Perfect'))
    ally_buff = models.IntegerField(default=0, choices=choiceList('Self', 'Ally gets Charm Benefits', 'Gain Supernatural Powers'))
    negation = models.IntegerField(default=0, choices=choiceList('None', 'Negate Penalties', 'Negate Requirement', 'Negate Normal Defense'))
    negation_detail = models.CharField(max_length=255, blank=True, null=True)
    speed_boost = models.CharField(max_length=255, default='None', choices=doubleChoices('None', 'Simple ⇒ Reflexive', 'Dramatic Action ⇒ Simple', 'Days ⇒ Dramatic Action', 'Months ⇒ Days'))
       # TODO: get essence cost of speed_boost
    unnatural_mental_influence = models.IntegerField(default=0,
                                                     choices=choiceList('None', 'Compulsion: Target resists w/ 1WP',
                                                                        'Intimacy: Target resists w/ 3WP (1wp to activate)',
                                                                        'Servitude Target resists w/ 5WP (2wp to activate)'))
    extra_willpower_to_resist = models.IntegerField(default=0, choices=choiceList('0 WP', '+2 WP (1wp to activate)', '+4 WP (2wp to activate)'),
                                                    db_column='additional_willpower_purchases')
    #other traits
    weakness = models.IntegerField(default=0, choices=((0, 'Normal'), (-1, 'Charm is easy to render Ineffective or Hard to Invoke  (Easily Overlooked, Immanent Glory)'),
                                                            (-2, 'Charm constrains the characters Available Actions (Bloodthirsty Sword Dancer)')))
    narrative_benefit = models.IntegerField(default=0, choices=choiceList(0, 1, 2),
                                            help_text="modifiers that don't fit within the usual system (Ghost-Eating)")
    counterattack = models.IntegerField(default=0, choices=((0, 'Normal'), (2, 'Counterattack')),
                                        help_text='Enables a DV 0 attack on the attacker when your turn comes up')
